I doubt there is an existing tool out there which does *exactly* what you describe

Here are a few tools which might get close enough to scratch your need:

`pip install xklb`

### Clustersort: 

This will organize the similar file name patterns next to each other even if they don't start with the same string.

Save the list of paths/files into a text file then use clustersort:

`lb clustersort files.txt sorted.txt`

### Substring prefix aggregation:

After creating a fs database with `lb fsadd` you can search fts and aggregate. This will give you the number of files, sum of file size, avg file size.


    lb fs my_fs.db -s abcd_00 -pa

Then you'll see something like:

    path | count | size
    Aggregate | 100 | 30 MB

You could also query the resulting SQLITE database directly instead of using `lb fs`

### Finding big folders

You might find the `lb bigdirs` command interesting (finds large folders similar to QDirStat or WizTree but with more granular options like substring / fts search as well as `--depth` or `--upper` / `--lower` min/max file count per folder to filter out folders from the results)

If your files are media files also look into `lb watch -R` (searches fts dynamically for the next media file based on words in the first video/song) and `lb watch -C` (does clustersort). Both of these options can be combined with `-B` which incorporates the bigdirs command in a weird serendipitous way. It's hard to explain but you can experiment with those three flags in different combinations to dive through a collection of large media

### Modifying disk-usage

You might find value in `lb du` command which is a weird combination of `du` and `lb bigdirs`. You can modify the source code [here](https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/disk_usage.py) to split on 7 char instead of "/" then you will basically have what you want I think ?
