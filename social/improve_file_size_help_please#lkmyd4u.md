`-b:v 8M` this means 8Mbit per second of data. At ~95 MB your video is around 90 seconds long, isn't it?

You can set `-b:v` to `0` to let ffmpeg use the `-crf` to determine the output bitrate

Also, vp9 (`libvpx-vp9`) is quite a bit better than vp8. x265 will also compress better than vp8

edit: here is a good guide with more info: https://slhck.info/video/2017/02/24/crf-guide.html
