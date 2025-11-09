> so let’s see some software setups

I [kept getting confused](https://github.com/chapmanjacobd/journal/blob/main/programming/linux/misconceptions.md#mv-src-vs-mv-src) with how `mv` decides to put folders and files. After writing [my own program](https://github.com/chapmanjacobd/library?tab=readme-ov-file#merge-mv) I can understand the reasoning for why it works like it does.

Most of the time I just use `rsync` and `mv`. But when I'm renaming stuff into folders that don't exist or when I'm merging folders in general I'll often reach for my program because it can work quite a bit faster than rsync if the files are on the same filesystem.
