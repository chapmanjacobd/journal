I like WizTree, SpaceSniffer on Windows

ncdu, QDirStat on Linux

I also wrote my own CLI which let's you search for interesting things. It should work on Windows, MacOS, and Linux:

    library du d1.db --parents -D=-12 --folder-size=+200G --file-counts=+5000
    path                                              size    count    folders
    ---------------------------------------------  -------  -------  ---------
    /                                              11.9TiB   125904      33837
    /mnt/                                          11.9TiB   125904      33837
    /mnt/d1/                                       11.9TiB   125904      33837
    /mnt/d1/check/                                 11.6TiB   122422      33596
    /mnt/d1/check/video/                           11.5TiB   111481      32433
    /mnt/d1/check/video/other/                      5.2TiB    37573       8505
    /mnt/d1/check/video/other/71_Mealtime_Videos/   3.2TiB    27921       7151
    /mnt/d1/check/video/Youtube/                    2.9TiB    51458      17289
    /mnt/d1/check/video/dump/                       2.5TiB    12294       3673
    /mnt/d1/check/video/dump/video/                 2.1TiB     8658       2549

I often use it with GNU Parallel to search multiple disks at the same time:

    parallel library du {} --parents -D=-12 --folder-size=+200G --file-counts=+5000 /folder_name/ ::: ~/disks/d*.db

The `/folder_name/` or path substring matching is optional. It caches to a database similar to ncdu so subsequent scans are fast and searching for different combinations of constraints only takes a few seconds.
