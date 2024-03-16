I wrote a python script to do this a couple weeks ago:

    $ pip install xklb
    $ library merge-folders -h
    usage: library merge-folders [--replace] [--skip] [--simulate] SOURCES ... DESTINATION

    Merge multiple folders with the same file tree into a single folder.

    https://github.com/chapmanjacobd/journal/blob/main/programming/linux/misconceptions.md#mv-src-vs-mv-src

    Trumps are files that are new or replaced files from an earlier source which now conflict with this later source.
    The count of conflicts also includes trumps.

If you don't choose --replace or --skip then it will ask you to choose after it scans everything and shows the statistics.

- https://github.com/chapmanjacobd/library#folder-subcommands
- https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/merge_folders.py
