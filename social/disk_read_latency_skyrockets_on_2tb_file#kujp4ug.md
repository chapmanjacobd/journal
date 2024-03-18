Unfortunately, firmware often doesn't let you know what is actually going on in the drive: running badblocks and checking SMART data is the most common generic way but you can try looking for specific tools that the drive manufacturer releases (if any)

But it sounds like, if the file is important, the next steps are to use `ddrescue` which can operate on both block devices and files, but you will have a better chance of recovering a file if you ddrescue the whole block device
