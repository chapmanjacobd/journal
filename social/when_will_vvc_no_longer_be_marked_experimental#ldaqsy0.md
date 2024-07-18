I think you need to use `-c:v libvvenc` ? not `-c:v vvc`? 

The docs on the page you linked to don't pass `-strict` and neither does [this article](https://chipsandcheese.com/2023/04/16/codecs-for-the-4k-era-hevc-av1-vvc-and-beyond/) from a year ago so something on your end is probably the issue

edit: I think there are some details in the ffmpeg changelog that might be helpful:

> 19/03/2024: Updated FFmpeg, vvenc, libopus and others. Official commit set native VVC decoder is experimental, now decodes default VVC video by using external libvvdec.

https://github.com/MartinEesmaa/VVCEasy/blob/master/FFMPEGVVC.md#limitations-of-ffmpeg-vvc-encoder
