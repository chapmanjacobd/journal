`-b:v 0 -crf 20` should be enough. I just learned that when -b:v is not set at all, ffmpeg will choose a default of 200k for vp8. This is different behavior from the x264 encoder. 

https://superuser.com/a/1280369/76968
