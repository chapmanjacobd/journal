> duplicates ... like the normal film and the directors version

I made a program that will show you folders with similar names--that might be helpful here.

[similar_folders.py](https://github.com/chapmanjacobd/library/blob/main/library/folders/similar_folders.py)

When printing folder groups it includes file count, total folder size, and median file size. You can use it like this:

    pip install library
    library similar-folders --filter-names .\videos\

It has different options for filtering groups based on duration, size, and full path. Use `--help` to see them all

There's also another script for [just filenames](https://github.com/chapmanjacobd/library/blob/main/library/files/similar_files.py) instead of foldernames
