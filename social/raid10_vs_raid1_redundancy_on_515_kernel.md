There is a lot of older information about btrfs RAID10 and I want to know if 2 btrfs RAID1 groups offer any more redundancy than 1 btrfs RAID10 group (4 disks).

Is it still true that btrfs RAID1 and RAID10 can only survive one drive loss, even with more than the minimum required drives?

With 2 btrfs RAID1 groups, I'm assuming that it would be possible to lose any one drive and up to two specific drives. Is this also true for btrfs RAID10?

If no, do raid1c3 or raid1c4 metadata change the scenario at all? Is a 2 disk loss in a 4 disk btrfs RAID10 group always a total loss of files or is it only a loss of ~25% of blocks/files?
