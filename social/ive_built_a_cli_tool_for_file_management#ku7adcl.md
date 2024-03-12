`ncdu` has export/import functionality

But you might be interested in `lb du`, `lb fs`, and possibly `lb bigdirs`

You can scan a folder and add all the files to a sqlite database. 

    $ lb fsadd --fs disk3.db /mnt/d3/

Then you can search and aggregate filtered files. Here are a few different examples:

The disk-usage subcommand will show folders at the first depth where there is more than one item (in this case depth 3):

    $ lb du audio.db 
    path                          size    count
    ------------------------  --------  -------
    /mnt/d/80_Now_Listening/   3.9 GiB      302
    /mnt/d/sync/              98.8 GiB    16699
    2 paths at current depth (2 folders, 0 files)

You can set folder depth explicitly:

    $ lb du audio.db -d6
    path                                                         size    count
    ------------------------------------------------------  ---------  -------
    /mnt/d/80_Now_Listening/weekly/83_Classical_Composers/   42.2 MiB        1
    /mnt/d/sync/audio/music/                                  4.7 GiB      131
    /mnt/d/80_Now_Listening/weekly/82_Audiobooks/             3.5 GiB      230
    /mnt/d/sync/audio/weekly/                                94.1 GiB    16568
    /mnt/d/80_Now_Listening/weekly/81_New_Music/            296.9 MiB       67
    /mnt/d/80_Now_Listening/weekly/Haircuts_For_Men/          6.9 MiB        2
    /mnt/d/80_Now_Listening/weekly/83_Classicalcomposers/     2.8 MiB        2
    7 paths at current depth (7 folders, 0 files)

And you can search for specific things with `-s`

    $ lb du audio.db -s Mixtape
    path                                                  size    count
    -----------------------------------------------  ---------  -------
    /mnt/d/sync/audio/weekly/81_New_Music/unsorted/  135.2 MiB        8
    /mnt/d/sync/audio/weekly/81_New_Music/reddit/    402.9 MiB       38
    /mnt/d/sync/audio/weekly/81_New_Music/bandcamp/    3.6 MiB        1
    /mnt/d/sync/audio/weekly/81_New_Music/youtube/     3.4 MiB        1
    4 paths at current depth (4 folders, 0 files)

Only aggregate files that are smaller than 1MB. This uses the same syntax as fd-find (so use -S+1M for >1MB)

    $ lb du audio.db -d6 -S-1M
    path                                                        size    count
    -----------------------------------------------------  ---------  -------
    /mnt/d/80_Now_Listening/weekly/83_Classicalcomposers/  627.4 KiB        1
    /mnt/d/80_Now_Listening/weekly/82_Audiobooks/            6.6 MiB       17
    /mnt/d/sync/audio/weekly/                              379.5 MiB     1127
    /mnt/d/80_Now_Listening/weekly/81_New_Music/             1.1 MiB        5
    4 paths at current depth (4 folders, 0 files)

- `lb fs` will open the files one at a time... it might default to 10 seconds per file or it might wait until you close the program that the file opens with (xdg-open) I don't remember--I mostly use this with media files
- `lb fs -p` will print a table
- `lb fs -pa` will print an aggregate table
- `lb fs -pf` will print a pipe-able list of files

There are many ways to filter and sort. Try `lb fs -h` to get some ideas

    $ lb fs disk3.db --ext mka -pa
    path         count  duration               avg_duration             cadence_adj_duration        size    avg_size
    ---------  -------  ---------------------  -----------------------  ----------------------  --------  ----------
    Aggregate       36  3 hours and 2 minutes  5 minutes and 3 seconds  1 hour and 43 minutes   80.7 MiB     2.2 MiB

https://github.com/chapmanjacobd/library

Disclaimer: I'm one of the maintainers
