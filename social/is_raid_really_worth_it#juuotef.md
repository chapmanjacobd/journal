RAID is definitely important for business continuity circumstances. If you are storing customer data, whether or not customers are directly accessing that data, you should be using something like RAID or [erasure coding](https://en.wikipedia.org/wiki/Erasure_code#Optimal_erasure_codes_2) in addition to regular backups and backup testing.

But not all data is worthy of redundancy. I personally value extra storage space above minimizing downtime. Is it likely that one of my drives will die in the next 10 years? Yes, maybe 5% to 20% chance. If I _needed_ the data then I wouldn't take that chance.

The worst part about losing a drive would be not knowing what was lost. That's why I scan everything weekly and backup all the metadata to multiple places as well as backup the data that I actually care about--when a drive fails it will take a few minutes or maybe hours to rsync the important stuff back (if it was stored on that drive), not a lot of data relative to everything else so not a huge benefit to RAID there.

I use `mergerfs` to have partial continuity. If a drive fails then I lose random files. I even wrote a script to [make the file loss more random](https://github.com/trapexit/mergerfs-tools/issues/39#issuecomment-1414592026) so that I still have a lot of media that I can watch or listen to while things [redownload](https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/redownload.py). If I lose stuff forever then it is the same as if I used RAID1 and never downloaded them ;-)

Actually, I [previously accidentally deleted 12TiB](https://github.com/andreafrancia/trash-cli/issues/286) and RAID wouldn't have helped in this scenario but neither did the partial continuity of `mergerfs`. But in the end I was able to redownload almost everything
