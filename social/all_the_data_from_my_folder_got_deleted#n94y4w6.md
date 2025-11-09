> but paused it due to low storage space on my computer

Did you delete files temporarily on your computer to recover free space? If so, that's likely why. Even if you closed Syncthing while deleting stuff--if it sees the files there before and the next time it scans they aren't there then the only thing it can assume, as long as the `.stfolder` is still there, is that the files were deleted

I'm not a Syncthing dev just a user. I've had Syncthing do unexpected things before but if you check your Syncthing logs you'll likely see it making logical choices. If you want something more manual maybe you could try FreeFileSync or rsync.

> recovery

Did you try [PhotoRec](https://www.cgsecurity.org/wiki/TestDisk_Download)? hope you can undo your loss
