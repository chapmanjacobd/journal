Git Annex lets you know what files are on which disconnected drive (USB, sshfs, anything that is a block device).

Another idea is that you can save the output of tree or a program like [QDirStat](https://github.com/shundhammer/qdirstat/issues/97) or SpaceSniffer if you're on Windows.

They both have an option to export the list of files in a variety of sorting. you can take snapshots of the list of files periodically over time and diff between the list to see what files changed (added or deleted)

 since they are text files you can commit them to a git repo and manage your changes when writing additional metadata like tags about the files, or grepping the output to quickly find files (faster than scanning the hard drive xattr tags)
