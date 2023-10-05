Don't use any RAID (RAID1 isn't as bad but you'll still have problems) on external devices. I second the advice to use mergerfs.

You can backup files to other disks and have recoverability since the last time that you backed up.

For example, if you have four disks that you want to mirror:

    rsync -auh --info=progress2 --no-inc-recursive /mnt/d1 /mnt/d2
    rsync -auh --info=progress2 --no-inc-recursive /mnt/d3 /mnt/d4
