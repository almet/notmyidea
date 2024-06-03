---
title: Start a process when using pytest-xdist
tags: django, tests, pytest
---

Here is how to start a process inside a test suite, using a pytest fixture. This comes
straight from [this post](https://til.simonwillison.net/pytest/subprocess-server).

```python
def run_websocket_server(server_running_file=None):
    ds_proc = subprocess.Popen(
        [
            "umap",
            "run_websocket_server",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    time.sleep(2)
    # Ensure it started properly before yielding
    assert not ds_proc.poll(), ds_proc.stdout.read().decode("utf-8")
    yield ds_proc
    # Shut it down at the end of the pytest session
    ds_proc.terminate()
```

This works well in general, but when using [pytest-xdist](https://pytest-xdist.readthedocs.io/en/stable/)
to distribute the tests on multiple processes, the server will try to be started
multiple times, where we want it to start only once.

It is possible to mark the tests you want to group together to run on
the same process, using "load groups":

```python
@pytest.mark.xdist_group(name="websockets")
def test_something(websocket_server):
  # do something here.
```

When running the tests, you will need to pass a flag to pytest:

```bash
pytest --dist=loadgroup
```
---

## A messier solution using file locks

Here is another solution I wrote, which is more involved and… messier.

Still, I'm putting it here in case it helps later on. Basically, it is using
files as inter-process communication.

You've been warned, you don't need to read this. If possible, use the version at
the beginning of this post instead.

```python
@pytest.fixture(scope="session")
def websocket_server(tmp_path_factory, worker_id):
    # Because we are using xdist to paralellize the tests, the "session" scope can
    # happen more than once per test session.
    # This fixture leverages lockfiles to ensure the server is only started once.

    if worker_id == "master":
        # This only runs when no workers are used ("pytest -n0" invocation)
        yield from run_websocket_server()
    else:
        # The first runner getting there will make the others wait on it
        # Two files are at play here. the first selects one worker to start the server
        # And the second one tells other workers the server is up and running
        temp_folder = tmp_path_factory.getbasetemp().parent
        lock_file = temp_folder / "ws_starting.lock"
        server_running_file = temp_folder / "ws_running"

        def _wait_for_server():
            while not server_running_file.exists():
                time.sleep(0.1)

        if not lock_file.exists():
            # Start the server
            with temporary_file(lock_file) as server_starting:
                if server_starting:
                    yield from run_websocket_server(server_running_file)
                else:
                    _wait_for_server()
                    yield
        else:
            _wait_for_server()
            yield


def run_websocket_server(server_running_file=None):
    # Find the test-settings, and put them in the current environment
    settings_path = (Path(__file__).parent.parent / "settings.py").absolute().as_posix()
    os.environ["UMAP_SETTINGS"] = settings_path

    ds_proc = subprocess.Popen(
        [
            "umap",
            "run_websocket_server",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    time.sleep(2)
    # Ensure it started properly before yielding
    assert not ds_proc.poll(), ds_proc.stdout.read().decode("utf-8")

    # When the server has started, create a file to tell the other workers
    # they can go ahead.
    with temporary_file(server_running_file):
        yield ds_proc
        # Shut it down at the end of the pytest session
        ds_proc.terminate()

@contextmanager
def temporary_file(path):
    """Creates a temporary file, yield, and remove it afterwards."""
    if not path:
        yield
    else:
        try:
            with path.open("x"):
                yield True
            path.unlink()
        except FileExistsError:
            yield False
```

So, what happens here?

- When the tests are running without processes, we just run the websocket server ;
- When running with multiple workers, we use a lockfile, so that the first who
  gets there will block the other ones, until the server is started.
- The signal for letter the other processes that the server started is to write
   a file.

---

## Give me back `print()` when using pytest-xdist

Also worth noting that pytest-xdists makes it hard to use `print` statements
when debugging, because it captures output, even when using `pytest -s`

I found [this solution](https://github.com/pytest-dev/pytest-xdist/issues/354)
to help when trying to debug:

```python

@pytest.fixture(scope="session", autouse=True)
def fix_print():
    """
    pytest-xdist disables stdout capturing by default, which means that print() statements
    are not captured and displayed in the terminal.
    That's because xdist cannot support -s for technical reasons wrt the process execution mechanism
    https://github.com/pytest-dev/pytest-xdist/issues/354
    """
    original_print = print
    with patch("builtins.print") as mock_print:
        mock_print.side_effect = lambda *args, **kwargs: original_print(*args, **{"file": sys.stderr, **kwargs})
        yield mock_print    
```
