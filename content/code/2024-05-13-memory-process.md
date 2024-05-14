---
title: Know how much memory a long-running process used
tags: bash
---

I've had a situation in which I wanted to check the memory consumption of a
long-running process on my machine. For this, I discovered I can use the `time`
gnu utility (which is different from the bash `time`).

I didn't know it was possible to have this information this way, I'm always
using `top` (or `htop`) for stuff like this, but it doesn't get me the max
memory used :-)

On OSX, I had to install the gnu time with:

```bash
brew install gnu-time
```

And then, prepend `gtime -v` (ior `/usr/bin/time -v` on Linux machines):

```bash
gtime -v python umap/ws.py
```

Which got me a nice update once the process has finished:

```
Command terminated by signal 2
Command being timed: "python umap/ws.py"
User time (seconds): 1.67
System time (seconds): 0.91
Percent of CPU this job got: 5%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:45.92
Average shared text size (kbytes): 0
Average unshared data size (kbytes): 0
Average stack size (kbytes): 0
Average total size (kbytes): 0
Maximum resident set size (kbytes): 108160
Average resident set size (kbytes): 0
Major (requiring I/O) page faults: 184
Minor (reclaiming a frame) page faults: 13944
Voluntary context switches: 185869
Involuntary context switches: 7827
Swaps: 0
File system inputs: 0
File system outputs: 0
Socket messages sent: 1489
Socket messages received: 1491
Signals delivered: 1
Page size (bytes): 16384
Exit status: 0  
```
