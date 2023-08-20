Yes. I'm pretty confident that you will have no issues. 

I use `single` data and `raid1c3` metadata now as I realized that would best offer the availability which I want. For data redundancy I backup only the important stuff to a much smaller 13 TB system with the same `single`/`raid1c3` configuration. 

I recommend this; or `raid1` metadata if you have less than 4 disks

by the way, while you are waiting for your disks to convert it would be good if we could get more visibility on this issue. Do you mind sending a message to the btrfs mailing list? I am too lazy to figure out how to do that. I'm pretty confident that someone will be able to patch this edge case but I think right people don't really know about it
