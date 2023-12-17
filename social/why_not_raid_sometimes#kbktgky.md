> BTRFS "RAID1"

Just be careful with this. If you run out of metadata space then it's possible to get into a situation where even adding multiple drives to try to make the drive writable again is impossible: https://gist.github.com/chapmanjacobd/7022658b51ecfae8e5255398930a8d61

I love btrfs but multi-device btrfs has more edge-cases than normal. You won't lose your data but you'll have write downtime while you copy your data out of the filesystem into a new one. Ideally, `raid1` metadata would be better but right now `dup` metadata has fewer ENOSPC failure cases. I think mergerfs and btrfs (`dup` metadata, `single` data) is a powerful combination for a media server. 

For production use you should be constantly monitoring metadata free space... `mdadm` would have fewer surprises despite having more restrictions. If you follow the same restrictions as `mdadm` (multiples of same size of disks) you might have no problem with multi-device btrfs but that kind of defeats the point of btrfs
