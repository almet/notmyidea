---
title: Bust a specific podman cache entry
tags: podman, cache
status: draft
---

When building images using podman, cache entries are created for the different
steps of your `Dockerfile`. This makes subsequent commands run faster, by
hitting the cache rather than redownloading / computing what's needed.

There is a command to bust all the cache:

```bash
podman system reset
WARNING! This will remove:
        - all containers
        - all pods
        - all images
        - all networks
        - all build cache
        - all machines
        - all volumes
```

But I wanted to remove just a specific cache entry. I've had trouble finding it,
but it's possible to just prune a specific cache entry by doing:

```bash
podman rmi <cache-entry> -f
```
