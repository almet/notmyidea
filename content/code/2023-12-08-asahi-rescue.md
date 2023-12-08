---
title: Rescuing a broken asahi linux workstation
headline: How I used Alpine linux as a rescue system
tags: Linux, Asahi
---

On my main machine, I'm currently using [Asahi Linux](asahilinux.org/) (on a macbook m1). I've recently broken my system, which wasn't able to boot because of a broken `/etc/fstab`.

On my previous setups, I was able to easily plug an usb key and boot to it to solve my issues, but here I wasn't sure how to deal with it.

After playing a bit (without much luck) with [qemu and vagrant](https://github.com/leifliddy/fedora-macos-asahi-qemu/), someone pointed me to the right direction: using alpine linux.

Here's what I did to solve my broken install:

First, install this alpine linux on a key.

[Download the iso image here](https://dev.alpinelinux.org/~mps/m1/m1-usb-alpine-install.img.xz), and copy it to a key. I'm not sure why, but `dd` didn't work for me, and I ended up using another tool to create the usb from the iso. 

```bash
# When booting, press a key to enter u-boot. Then:
env set boot_efi_bootmgr
run bootcmd_usb0
```

Which should get you a session. When connected, do the following:

```bash
# to find the parition you want to mount, marked EFI something
lsblk -f
mount label="EFI - FEDOR" /mnt

# Install the wifi firmware
cd /lib/firmware
tar xvf /mnt/vendor/firmware.tar
/root/update-vendor-firmware
rm /etc/modprobe.d/blacklist-brcmfmac.conf
modprobe brcmfmac

# Connect to the wifi
/etc/init.d/iwd start
iwctl

```

In my case, I wanted to mount a btrfs filesystem to fix something inside.

```bash
apk add btrfs-progs
echo btrfs >> /etc/modules
modprobe btrfs
mount LABEL="fedora" /opt/fedora
```

I then could access the filesystem, and made a fix to it.

---

Resources:

- https://arvanta.net/alpine/install-alpine-m1/
- https://arvanta.net/alpine/iwd-howto/
- https://wiki.alpinelinux.org/wiki/Btrfs