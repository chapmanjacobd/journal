It's the same as selecting multiple audio tracks. You just need to `-map` it: https://trac.ffmpeg.org/wiki/Map

All major containers support multiple video streams but media player playback support might be lacking.

But I agree that it is usually better to have 1 video stream per file for the same reason that it is usually better to have one large GIS raster file instead of multiple bands. Software can decode/encode in parallel per file a lot easier than multi-thread writing to the same file. With the added benefit that the parallelism can be ignorant of implementation details like orchestrated with different software entirely (GNU Parallel, [outrun](https://github.com/Overv/outrun), etc)
