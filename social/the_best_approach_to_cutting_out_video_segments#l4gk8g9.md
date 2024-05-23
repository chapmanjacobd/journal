I think this might be a good starting point: https://github.com/mifi/lossless-cut/issues/126

But I don't think there really is a solution here other than cutting multiple times: https://trac.ffmpeg.org/wiki/Seeking#Seekingwhiledoingacodeccopy

edit: I think you can use the segment muxer to set accurate start and stop endpoints even if the -c copy actual data is a bit more
