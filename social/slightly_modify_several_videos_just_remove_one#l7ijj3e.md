I wonder if just changing the metadata with something like exifTool or ffmpeg would be enough to change the checksum. That would probably be the fastest.

Otherwise you could trim off the last second like this:

    ffmpeg -sseof -1 -i input.mp4 -c copy output.mp4

but trimming off the first frame will be faster because it only needs to decode the timestamps at the beginning of the file. Still, it will be slower than just editing metadata because ffmpeg will need to copy the whole file:

The only way to start at specific frames is to convert a number of frames to ss.ms syntax, or hh:mm:ss.ms. So, if your video is at 25 fps, and you want to start at frame 2, you would need to first calculate the timestamp:

2 / 25 = 0.08

    ffmpeg -i input.mp4 -ss 0.08 -c copy output.mp4

To run these tools on a bunch of files the easiest cross-platform way will probably be [fd-find](https://github.com/sharkdp/fd):

    fd -eMP4 -x ffmpeg -i {} blahblahblah ./out/{/}

This will put the outputs in a subfolder `./out/` https://github.com/sharkdp/fd?tab=readme-ov-file#placeholder-syntax

That being said...

> Then I modified one video

I'm guessing that you opened an NLE and made the cut that way? Then exported as "MP4" ? It's very possible that the video streams are a different codec after exporting from the NLE. MPEG4 [supports many](https://en.wikipedia.org/wiki/MP4_file_format#Data_streams) video codecs. It's a container--not a specific codec in its own right. It might help you to use `ffprobe` to check the video stream information. So you might actually still need to transcode the videos but it is not too difficult and you can use fd-find + ffmpeg to do that
