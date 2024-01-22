Yeah I think `btrfs` is a great filesystem but it can be a little awkward when running out of space because most filesystems treat free space much more simply--but running out of space in any filesystem is not good--and running out of free space in multi-device `btrfs` configuration throws another wrench/flamethrower into the works. I realize that what I'm saying here might not be applicable to you but I had a recent experience with having downtime due to this. 

The benefit of `btrfs` in a ENOSPC situation is that you can, at least theoretically, know for sure what writes were committed before running out of space. In practice, however, the additional complexity of getting back to a read/write filesystem becomes its own technical problem.

About a year ago I switched from multi-device `btrfs` to `mergerfs` backed by `btrfs`. Here is my [fstab](https://github.com/chapmanjacobd/computer/blob/main/.github/etc/fstab). 

To go from multi-device btrfs to this I had to move one device of data at a time via `sudo btrfs device remove /dev/sdX1 /mnt/d/`. It can take a while to run. It took 2-3 weeks in total. 

Is it worth the time to move stuff around? Maybe. I sleep a little better at night knowing that one or two drive failures will only lead to one or two drives of data to be lost--but besides that the only other benefit that I can think of is ease of removing a disk. Both mergerfs and multi-device btrfs add devices quickly. I would even say btrfs is slightly easier. But _removing_ a device with btrfs takes hours to days. `mergerfs` takes less than a second because it is just a configuration change and remount. But even if you want to move data off a disk to another disk it will take less time than `btrfs device remove`
