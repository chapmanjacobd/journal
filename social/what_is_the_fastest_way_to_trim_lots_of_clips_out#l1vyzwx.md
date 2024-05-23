https://trac.ffmpeg.org/wiki/Seeking

If you use mpv this script is really convenient. I use it almost daily and the results are nearly instant:

- https://github.com/chapmanjacobd/computer/blob/main/.config/mpv/scripts/mpv-splice.lua (be sure to adjust output_location)

Press Ctrl+T to set in and out points (you can have multiple per file but you need to set both in and out each time), 

Then when you are done press Ctrl+P to send the command to ffmpeg.
