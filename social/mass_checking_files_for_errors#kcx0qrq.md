yeah you would want to run this one file at a time. replace "$video" with the filename. 

If you aren't on Linux or Mac then you won't have `grep` but you should have [a similar utility](https://stackoverflow.com/questions/1485215/powershell-how-to-grep-command-output).

In addition to the above you might want to research exactly which bitrates and codecs are supported for your Firestick but you'll probably want to use a more expressive programming language at that point instead of shellscript so maybe it is best keep it simple by only checking `libx264` and if a file doesn't work smoothly it is probably too high bitrate like u/Anton1699 said.

There might be other apps that effectively do the above, perhaps even streaming the file so you only need to wait for the first part of a file to transcode before it starts playing. I don't use Amazon devices but with Chromecast you can use [catt](https://github.com/skorokithakis/catt/), VLC, and possibly ffmpeg to do this. For example, you can use `catt scan` to find the IP address and then do `vlc --sout '#chromecast' --sout-chromecast-ip=$ip --demux-filter=demux_chromecast --sub-file=my.srt my.mp4`. Maybe something similar exists for Amazon.
