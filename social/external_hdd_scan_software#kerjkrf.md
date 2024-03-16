I recommend using a modern filesystem which has built-in checksumming like btrfs.

If you want to scan large files quickly, I made [a hashing tool](https://github.com/chapmanjacobd/library#file-subcommands) which reads only tiny parts of files BUT anything that does a quick scan like this won't really help solve the problem that you want to solve. You have to read all the data in order to detect small bit-flips and corruption. It takes time to read 14TB of data. But luckily, if you are only storing video files they tend to be pretty forgiving so I wouldn't worry too much.
