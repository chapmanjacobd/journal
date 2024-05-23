Parallel rsync via fpart works great with millions of files: https://www.fpart.org/fpsync/

If you only care about file metadata and not directory metadata cpio+tar mode is a bit faster than rsync, but even in rsync mode it should be a lot faster for many small files than normal rsync
