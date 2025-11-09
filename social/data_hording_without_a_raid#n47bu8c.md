> I'm not hoarding anything really important on my NAS just stuff i would rather not have to find or download again

You need to think about the opportunity cost. If you lose a drive and need to download everything again--is your time worth it? If it takes 50 hours to find everything, and if $250 * 2 would have prevented this data loss (and you still need to pay $250 to buy another drive to replace the failed one), then your time is essentially worth $5/hour.

There's also the possibility that you won't be able to easily find what was previously easy to find.

If you are constrained by your budget, the economical solution is to have different tiers of data. If something is popular and easily found then you likely don't need to have duplicates locally. But I would definitely back up data that is important to you personally, less popular, or data that you think is relatively rare.

Also, the purpose of RAID is to reduce time during recovery. If recovery time is not an issue for you, a disconnected backup drive has its own benefits which you should evaluate against the availability aspect of RAID.

Also, mergerfs (and other union filesystems) are fun to play around with, but I've started using mergerfs less and less nowadays. Accessing disks directly is simpler and more performant. For example, write programs to [download to specific drives](https://github.com/chapmanjacobd/library/blob/main/library/multidb/allocate_torrents.py) depending on free space. Use programs like plocate to find files instead of creating and relying on complex folder hierarchies.
