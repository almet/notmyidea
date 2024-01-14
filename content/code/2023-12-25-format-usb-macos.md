---
title: Format an USB disk from the command-line on MacOSX
---

```bash
sudo diskutil unmountDisk /dev/disk5
sudo diskutil eraseDisk "MS-DOS FAT32" Brocolis /dev/disk
```
