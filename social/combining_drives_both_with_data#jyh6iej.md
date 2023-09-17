Just so you know, if you aren't doing this to use `raid1` data, doing this is more dangerous than leaving the drives separate. Btrfs will write `single` data blocks across devices so when one dies you _will_ lose [most of your data](https://gist.github.com/chapmanjacobd/bc6e31c8bc3647e0bcb0c43bc0464a9c#results) across BOTH disks. Even if you use `raid1` or more redundancy metadata. So if you are still planning on doing this you may as well use `raid0` data, `raid1` metadata. It is practically the same risk as `single` data.

You may want to use something like mergerfs instead. You can still balance files across disks in this scenario. I have 9 disks as separate btrfs filesystems with `single` data, `dup` metadata and [merge them this way](https://github.com/chapmanjacobd/computer/blob/main/.github/etc/fstab):

- https://github.com/trapexit/mergerfs-tools/issues/39#issuecomment-1414592026
- https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/scatter.py
