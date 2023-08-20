If you use `-d single` across multiple disks don't use `-m dup`, use `-m raid1`. `-m dup` should only be used in single-disk scenarios. 

As far as I know the risk of using `-d single` vs  `-d raid0` is almost exactly the same. So if you want the most disk space:

-  `-d raid0 -m raid1` (and remember to test your backups)

If you can get by with half the space, both of these options would allow you to lose one disk:

- `-d raid10 -m raid1` if you have at least 4 or 5 disks of similar sizes
- `-d raid1 -m raid1` if you have fewer than 4 disks

To be able to lose up to two disks you would need to use `-d raid1c3 -m raid1c3` (or maybe `-m raid1c4`? not sure)

Also, there is a difference between drive failure and file software corruption and silent hardware corruption. Corruption can happen from many sources. I believe that every btrfs option can detect silent corruption via metadata checksums but only RAID1 and RAID10 have the best chance of correcting the silent corruption on the fly.

btrfs RAID is different from normal RAID in that you have more flexibility in terms of mixing different disk sizes but with btrfs, regardless of whether you use single or a btrfs RAID mode, you will want to monitor that you have at least 5-15 blocks free (5 to 30GB+) free space so that btrfs has some room to work and breathe
