I was using btrfs raid10 data with raid1c4 metadata but 2 of my disks are larger than the others so I ran out of metadata space with 8TB data space and I was getting "parent transid verify failed" errors. 

Thankfully it remounted itself as read-only and it was easy to mount it as `-o rw,usebackuproot` then run balance to switch metadata to raid1 so that I can use the 8TB free space--everything is working fine now but it would be nice to be able to use raid1c3 or c4.

Is there a way to mark the remaining ~50GB on three of my other drives (total 150GB) as only to be used for metadata?--or at least until all drives have the same amount of unallocated space.
