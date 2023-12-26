This sounds like you need to use `-ss` after the input file `-i`:

## Input seeking

When -ss and -t are placed before the input, ffmpeg resorts to fast seek which relies on the index of the input to allow ffmpeg to start and stop seeking. Some formats don't have indices, so ffmpeg estimates duration via bitrate. This can be inaccurate.

## Output seeking

When -ss and -t are placed after the input, ffmpeg counts demuxed packets. This will be accurate but a lot slower.

You can use both at the same time but you may need to subtract some lead-in time for ffmpeg to seek to the accurate timestamp properly (how much depends on the format).

https://trac.ffmpeg.org/wiki/Seeking#Combinedseeking
