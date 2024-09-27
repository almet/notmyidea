---
title: Deploying on fly.io
tags: docker, deployment, websockets
---

I spent some time today deploying [uMap](https://umap-project.org) to [fly.io](https://fly.io), using a `Dockerfile`. Here are some notes I took.

First, I had to install the `flyctl` command. On OSX, with `brew`, it's:

```bash
brew install flyctl
```

Fly is using docker containers under the hood, and provides some tools to help  create the files. In the case of uMap, I already had a `Dockerfile`, so it wasn't necessary.

## Creating an app

I created an app:

```bash
fly apps create
```

By answering the questions. It eventually generated a `fly.toml` file., that I actually rewrote to fit my needs:

```toml
app = 'umap'
primary_region = 'iad'
console_command = 'umap shell'

[build]
  dockerfile = "Dockerfile"

[[services]]
  internal_port = 8000
  protocol = 'tcp'
  processes = ["app"]

  [[services.ports]]
    handlers = ['http']
    port = 80
    force_https = true

  [[services.ports]]
    handlers = ['http', "tls"]
    port = 443

[[vm]]
  memory = '1gb'
  cpu_kind = 'shared'
  cpus = 1
```

The `services` section could be simplified by using the `http_service` section, but as I will need to configure websockets on a different port, it seems to be a better bet.
## Creating PostgreSQL / PostGIS database

I created a postgres app, that I named `postgres_umap` by answering the questions asked by this command:

```bash
flyctl postgres create
```

Then I had to activate the PostGIS extension, by connecting to the postgres cluster…

```bash
flyctl postgres connect -a postgres-umap
```

… and enter this:

```
CREATE EXTENSION postgis
```

At this stage, the machine crashed, and a `fly logs -a postgres-umap` told me that it was out of memory. I bumped the memory a bit with this:

```bash
# got the id of the machine with
fly machine status -a postgres-umap
# and then bumped the memory to 1024mb
fly machine update 3d8dd964a25978 --vm-memory 1024 --app postgres-umap
```

Redoing the `CREATE EXTENSION postgis;` worked this time.

Once this is done, I used this utility:

```bash
fly postgres attach postgres-umap --app umap
```

This created users, passwords and a database for me, and set the proper secrets for my app. Neat. 

I received an email telling me this costs money, so after initializing the postgis database, I scaled the instance down:

```bash
fly machine update 3d8dd964a25978 --vm-memory 256 --app postgres-umap
```

## Handling secrets

Additionally to environment variables (which are present in the `fly.toml` file), I also had to define some secrets, using `fly secrets`:

```bash
secrets set SECRET_KEY=S0_S3CR3T
```

At some point, I had to unset some of them with: 

```bash
secrets unset SECRET_KEY
```

I also added a few env vars:

```toml
[env]
  WEBSOCKET_URI = "wss://xxx.fly.dev:8001"
  WEBSOCKET_HOST = "0.0.0.0"
  WEBSOCKET_ENABLED = "True"
  UMAP_ALLOW_ANONYMOUS = "True"
```

## Deploying

With this in place, I could deploy these two machines with `fly deploy`.

## Adding support for WebSockets

This can change in the future, but for now, I have two servers, a WebSocket server listening on port `8001`, separate from the `uwsgi` server listening on `443` and `80`.

It is possible to define some specific commands that will replace the default `CMD` one of the `Dockerfile`. 

To do this, I used the `[processes]` section, and named the default one `django`, because it's running the django server with `uwsgi`:

```toml
[processes]
ws = "/venv/bin/python /venv/lib/python3.11/site-packages/umap/ws.py"
django = "/srv/umap/docker/entrypoint.sh"
```

… and added a new services definition:

```toml
[[services]]
    internal_port = 8001
    protocol = 'tcp'
    processes = ['ws']
    
    [[services.ports]]
      handlers = ['tls']
      port = 8001
```

Also, I'm not sure why I had to downgrade the number of processes:

```bash
fly scale count 1 --process-group=django
fly scale count 1 --process-group=ws
```

## Using a custom domain

I wanted this to be hosted on my domain, so I went with adding a `CNAME`, following [this documentation](https://fly.io/docs/networking/custom-domain/):

```bash
CNAME 	xxx 	xxx.fly.dev
```

And then generated the SSL certs:

```bash
fly certs add xxx.domain.tld
```

## Persisting files

Everything was working smoothly until I realize that the files weren't actually persisted. For the files to be persisted, I needed to add volumes in the toml file:

```toml
[mounts]
  source="umap_data"
  destination="/srv/umap/uploads"
```

And create the volumes with the cli:

```bash
fly volume create umap_data -r iad -n2
fly deploy
```

## The final file

Here is the final `fly.toml` file I came up with:

```toml
app = "umap"
console_command = "umap shell"
primary_region = "iad"

[build]
dockerfile = "Dockerfile"

[env]
SITE_URL = "https://umap-dev.notmyidea.org"
UMAP_ALLOW_ANONYMOUS = "True"
WEBSOCKET_ENABLED = "True"
WEBSOCKET_HOST = "0.0.0.0"
WEBSOCKET_URI = "wss://umap-dev.notmyidea.org:8001"

[[mounts]]
destination = "/srv/umap/uploads"
source = "umap_data"

[processes]
django = "/srv/umap/docker/entrypoint.sh"
ws = "/venv/bin/python /venv/lib/python3.11/site-packages/umap/ws.py"

[[services]]
internal_port = 8_000
processes = [ "django" ]
protocol = "tcp"

  [[services.ports]]
  force_https = true
  handlers = [ "http" ]
  port = 80

  [[services.ports]]
  handlers = [ "http", "tls" ]
  port = 443

[[services]]
internal_port = 8_001
processes = [ "ws" ]
protocol = "tcp"

  [[services.ports]]
  handlers = [ "tls" ]
  port = 8_001

[[vm]]
cpu_kind = "shared"
cpus = 1
memory = "1gb"  
```
