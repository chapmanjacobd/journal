well if you are going to wipe the disk and start over I would recommend running this just to get rid of any extra stuff that ~might~ be there

    sudo wipefs -af /dev/sdk

Then create a partition with gdisk

    sudo gdisk /dev/sdk
    n
    8300
    w

    sudo mkfs.btrfs -m dup -d single /dev/sdk1 -L disklabel

edit: if you accidentally ignored the "Partition table header claims that the size of partition table entries is 0 bytes" and "THIS WILL OVERWRITE EXISTING PARTITIONS!!" warning you could still try to recover data with testdisk: 
https://forum.cgsecurity.org/phpBB3/viewtopic.php?t=8399 https://www.cgsecurity.org/wiki/TestDisk_Download
