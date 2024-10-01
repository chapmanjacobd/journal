It really depends on the cause of the drive failure. Drives fail for a lot of different reasons. It's reasonable to only run `ddrescue`, but if there are a few specific files that are much more important than the other contents of the drive then I would attempt to copy those first, maybe using ddrescue in file input mode. But if the filesystem is broken there aren't a lot of options that are better than running `ddrescue` for the whole partition or disk

https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html#Algorithm
