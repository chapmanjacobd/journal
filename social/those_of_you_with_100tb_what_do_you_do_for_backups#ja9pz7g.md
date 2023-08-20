I only backup stuff that I've seen before and liked. Unwatched stuff is spread across a JBOD array of btrfs (so I get the benefit of bitrot detection) single-mode and accessed via mergerfs (here is my [fstab](https://github.com/chapmanjacobd/computer/blob/1d2dd123e1f23f5185bdb568171093d7d8fe2505/.github/etc/fstab#L28) config). I feel very confident now that losing a drive will not impact me very much.

Yes, I could lose 10TB of data but it's all random. I even wrote a script to make files [even more randomly distributed](https://github.com/trapexit/mergerfs-tools/issues/39#issuecomment-1414592026).

Losing a drive is likely but not *that* likely. Media is much more likely to disappear from the internet. 

Losing the data from the hard drive AND the internet is less likely than just one of those events happening. Recently I accidentally deleted 12 TB of media and I was able to [redownload](https://github.com/chapmanjacobd/library/blob/main/scripts/redownload.py) 80% of it using a script that I wrote. 20% of it I had to manually redownload but everything was still there.
