If you ever end up publishing this I would be interested to see how you tackle some of these problems.

> fast cache of the data

This is probably the easiest thing to solve. If you grab all the paths from whatever database you store the data in then subtract that set from a set of scanned files. I've done this before here: [fs_extract.py#L271](https://github.com/chapmanjacobd/library/blob/main/xklb/fs_extract.py#L271) and it works really well. But if you want to support multiple "canonical" paths or don't have a way to figure out which path is canonical between mergerfs, nfs, etc then you might need to get creative with how you use the index 

#### more optional:

To speed up the file listing part of file scanning you can have a `dump/` folder ([mktree.py](https://github.com/chapmanjacobd/computer/blob/main/bin/mktree.py)) and move them into another folder after scanning. I've started to do this as well for various reasons (but note that this contradicts the above "indexing" so subtracting the sets doesn't do anything useful unless you decided to rescan the folder where scanned files were moved to because the moved files have a different folder prefix). This is what my video import command looks like; but it doesn't do everything that you've listed:

    lb fsadd ~/lb/video.db --hash --delete-unplayable \
      --move ~/d/check/video/ --check-corrupt \
      --full-scan-if-corrupt 15% --delete-corrupt 20% \
      ~/d/dump/video/
