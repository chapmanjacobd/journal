pretty sure you can do this:

    ffmpeg -i {} -map 0:1 -map 0:2 -map 0:4 -c copy output1.mkv -map 0:1 -map 0:3 -map 0:5 -c copy output2.mkv

edit: added `-c copy`
