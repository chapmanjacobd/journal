> filled it with 99% data and now BTRFS shows NO errors

be sure that you are running btrfs scrub between those two steps. Otherwise there hasn't really been a check on the data.

If disks were more expensive, I think there would be a big opportunity in this space for partial fault tolerant filesystems at the file level. This is similar to how AWS S3 works. You might want to use both `dup` metadata and `dup` data.

But as your disk degrades it will become increasingly likely that both copies of your filesystem metadata will be unreadable. So I would recommend only storing data there which you wouldn't mind losing. At maximum you could use this drive as ONE of your backup drives. It shouldn't be your main drive.

I kind of do this, I don't use RAID because partial continuity is good enough for me: https://old.reddit.com/r/DataHoarder/comments/15icgo7/is_raid_really_worth_it/juuotef/?context=3
