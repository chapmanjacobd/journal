ddrescue is one of the few tools that can actually recover data when other tools can't--but depending on the drive failure I would first try to copy out the important files normally because ddrescue can be much more intensive than normal read/write patterns; the disk *could* theoretically fail before the most important sectors are read.

It's also possible to run ddrescue on specific files (`if=file.txt`) so it might make sense to attempt that first... however you'll have a better chance of recovering file.txt with a full disk read
