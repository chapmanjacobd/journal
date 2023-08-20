Consider using `compress-force=zstd:2`

> with compress, if the first 64KiB of a file is not compressible, Btrfs will not even attempt to compress the rest of the data. Compress-force meanwhile will attempt to compress the entire file, even if the first 64KiB isn't compressible (which can definitely be the case for many files).

https://forums.unraid.net/bug-reports/prereleases/consider-using-compress-force-instead-of-compress-for-btrfs-compression-r2326/
