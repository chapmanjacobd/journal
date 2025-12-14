Here's one way of doing it:

    pip install library
    library mv --ext jpg,jpeg,png,pdf,tiff,tif,bmp,webp /mnt/src1/ /mnt/src2/ /mnt/dest/images/ --dry-run

If you like the output, just remove --dry-run. If you want to copy, use `cp` instead of `mv`

You can also run

    library exts /mnt/src1/

to see a count of file types and their total sizes
