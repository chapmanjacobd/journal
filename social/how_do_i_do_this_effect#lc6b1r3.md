It totally depends how quickly your camera can shoot stills and the look that you're going for.

You can try processing with ffmpeg to extract only the I-Frames:

    ffmpeg -i in.mov -an -sn -filter:v "select='eq(pict_type,PICT_TYPE_I)',setpts=N/FRAME_RATE/TB" out.mov

This might be an interesting effect in of itself but you'll probably want to override the fps explicitly. Replace `out.mov` with `-r 1.2 out.mov` to have one frame per 1.2 seconds (1.2 fps * 60 seconds = 72 bpm).

You'll want to adjust the input frame rate as well. To do this you'll set `-r 0.6` BEFORE the input file `-i`. I think you should technically set this to number of I-frames that you expect from your source, but you could also set it to any number. It's a creative choice. A multiple of the bpm might work well too. For example, 0.6 or 2.4. So your full command might look like this:

    ffmpeg -r 0.6 -i in.mov -an -sn -filter:v "select='eq(pict_type,PICT_TYPE_I)',setpts=N/FRAME_RATE/TB" -r 1.2 out.mov

You can inspect how many I-frames per second using something like this command:

    ffprobe -v error -of default=noprint_wrappers=1:nokey=1 -select_streams v -skip_frame nokey -show_frames -show_entries frame=pkt_dts_time in.mov | head

Alternatively, don't set any fps and replace `out.mov` with `'%05d.bmp'` to extract images instead--that way you'll have more control over how long each image is displayed within your NLE:

    ffmpeg -i in.mov -an -sn -filter:v "select='eq(pict_type,PICT_TYPE_I)',setpts=N/FRAME_RATE/TB" '%05d.bmp'

If your camera has an option to force ALL frames to be I-Frames (maybe via recording "RAW" or an external recorder) then you can replace `'eq(pict_type,PICT_TYPE_I)'` in any of the above commands with something like `'not(mod(n,5))'` 

https://superuser.com/questions/1156837/using-every-nth-image-in-sequence-to-create-video-using-ffmpeg

You can also play around with the number of duplicated frames. For example, here we only take every 16th frame and we show it for 4 frames:

    ffmpeg -i in.mov -an -sn -filter:v "select='not(mod(n\,16))',setpts=N*4/FRAME_RATE/TB" out.mov

Actually, I guess this should be a simple duration instead of dividing by frame rate. `N/TB` will show each frame for one second:

    ffmpeg -i in.mov -an -sn -filter:v "select='not(mod(n\,256))',setpts=N/TB" out.mov

An approach like this combines filtering non-keyframes and skipping some:

    ffmpeg -skip_frame nokey -i in.mov -an -sn -filter:v "select='not(mod(n\,2))',setpts=N*0.25/TB" out.mov

Here 117 is BPM. You can replace `/TB` with `/2/TB` for double-time or `*2/TB` for half-time. Replace `-f matroska - | ffplay -` with `out.mov` to save a file instead of previewing it as it renders

    ffmpeg -i in.mov -an -sn -filter:v "select='not(mod(n\,256))',setpts=N*(60/117)/TB" -f matroska - | ffplay -

You can also use a bunch of images as input (instead of video):

    ffmpeg -i 'in_%05d.jpg' -filter:v "setpts=N*(60/117)/TB" out.mov

but you'll probably want to scale it and choose a specific output format rather than relying on defaults:

- https://stackoverflow.com/questions/52673706/how-to-crop-and-scale-correctly-with-ffmpeg
- https://askubuntu.com/questions/907398/how-to-convert-a-video-with-ffmpeg-into-the-dnxhd-dnxhr-format
