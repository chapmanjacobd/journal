Is it possible to mount my btrfs filesystem with a drive "soft"-unplugged, see what files I'm able to access then remount it a couple hours or days later with the disk attached again?

I want to write a few scripts to help with redownloading / restoring from offsite backups and it would help to be able to temporarily simulate a disk failure--but I don't want to actually lose data or have to unplug and replug the disk...

I'm running single mode data with raid1c3 metadata.

EDIT: I made a script to simulate how much data would be lost and it is available here (data lost is printed as Data-device dependence; but you will separately also need to consider the redundancy of your metadata) : https://github.com/knorrie/python-btrfs/pull/40
