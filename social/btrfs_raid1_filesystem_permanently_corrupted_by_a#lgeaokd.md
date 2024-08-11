Yeah I also hit a weird edge case with raid1 mode relatively recently: https://gist.github.com/chapmanjacobd/7022658b51ecfae8e5255398930a8d61

I can't remember if I was able to salvage it--just remember spending a full day or so trying. I think I had to `wipefs` and start over

btrfs single mode is solid. I would probably use mdadm if I wanted RAID1 in the future, but after playing around with different RAID configurations I realized that I don't actually need it. It takes less than a day to restore from backup
