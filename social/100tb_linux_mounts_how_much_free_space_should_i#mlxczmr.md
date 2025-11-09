Yeah btrfs has a global reserve which often helps prevent unrecoverable situations:

    $ sudo btrfs fi usage /mnt/d1
    ...
    Global reserve:		512.00MiB	(used: 16.00KiB)
    ...

It works 99% of the time but it is still very possible to get into a situation where you are out of space and btrfs won't allow you to add a disk to the filesystem
