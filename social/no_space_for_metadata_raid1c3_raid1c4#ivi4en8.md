> add a temporary disk to the system now to rebalance the metadata, just enough space to get delete working again, and then remove that disk from the array once I've freed up enough space on the filesystem

yes that is definitely possible.

my advice: Be careful mounting with backuproot if you aren't going to fix the issue. But if it is mounting as read-only then it's probably fine until you can fix it.

> deleting files seems to have no effect on the amount of free space

It sounds like it is not read-only if you are able to delete files. You might try running:

    sudo btrfs fi balance start -musage=0 /mntpoint
    sudo btrfs fi balance start -dusage=0 /mntpoint

This will free up any unused blocks. It should be harmless to run in all cases; though it might not fix your issue

>  After a reboot I was able to start a rebalance with raid1 metadata, but even that ran out of space while rebalancing

can you paste the output of 

    sudo btrfs de usage /mntpoint
