I agree that is a bad argument. Although, if that is your only insight from the page I would argue that you have done both a strawman and an ad hominem.

However:

    uncompressed              7m57.281s     311GB        651.61MB/s
    compress=zstd:3           7m41.138s     306GB        674.42MB/s
    compress-force=zstd:3    13m43.869s     163GB        377.49MB/s

This is compelling. 

I've found similar space savings on some extents when switching to `compress-force=zstd:2` when I moved from a multi-device setup to multiple single devices (I transferred all the data out of an array (~80TiB) so it was all recompressed with the new fstab setting).

After everything copied over I don't remember exactly how much extra free space I had, I would say tens more TiB but that sounds unbelievable right? I know I had at least 4TiB more free space.
