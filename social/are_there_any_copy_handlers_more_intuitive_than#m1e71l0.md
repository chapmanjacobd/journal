I wrote a command line tool that has a lot of options. You set all the file conflict possibilities before-hand and it will never ask to confirm anything (the only exception is if you choose the `--file-over-file delete-dest-ask` fallback option)

    pip install xklb
    library cp /mnt/src/s1/ /mnt/dest/s1/

This will use a SHA-256 file hash by default to determine that conflicting files are duplicates. If the match fails then it will rename the existing destination file to `..._1.ext`. 

If you only want to check the file size, which is quite a bit faster, you can add this: `--file-over-file 'skip-size rename-dest'`, or if you trust your target is more recent than the source `--file-over-file 'skip-size rename-src'` to rename the non-equal _source_ files to `..._1.ext`.
