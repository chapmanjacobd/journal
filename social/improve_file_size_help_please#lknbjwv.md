basically the idea is to copy the bitrate from the input video.

I don't know batch that well but in nushell (which can run on windows) I just tested this and it works for me:

    for file in (ls *.mp4 | get name) {
        print $file
        let bitrate = (ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 $file)
        ffmpeg -hide_banner -loglevel warning -stats -i $file -c:v libvpx -b:v $bitrate -c:a libvorbis ($file | path parse | update extension webm | path join)
    }

The file that I end up with is almost the same size:

    .rw-r--r--@ 212M xk   30 Aug 17:56  426.mp4
    .rw-r--r--@ 204M xk   30 Aug 17:59  426.webm

Visually I can't tell the difference when playing the files side by side. That being said, you could probably get a smaller filesize than x264 by targeting a lower bitrate (because vp8 might compress better) -- you could replace `$bitrate` above with `($bitrate * 0.8 // 1)` to target 20% smaller than input filesize
