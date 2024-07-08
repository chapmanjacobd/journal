thanks for including the full output of that. You definitely need to use the `-` in `-filter_complex` but maybe you don't need [a] at the end of the filter_complex: https://superuser.com/questions/1615898/ffmpeg-filter-complex-connecting-outputs

> use a standard extension for the filename or specify the format manually

Oh I guess you also need to add `-c:a pcm_s24le` or something like that

Using the above ffprobe information, I think we can still use `[0:a:0][0:a:1]` but you can also use `[0:0][0:1]`. I don't think it actually matters because the muxer will only include streams that make sense.

If it still doesn't work after specifying the output audio format with `-c:a`. I think what we are missing is a map at the end. In this case, you'll need `[a]` at the end of the -filter_complex string and then `-map 0:v -map [a]` right before the output filename. Or maybe you can use `-map 0 -map -0:a -map [a]` to keep the timecode stream too
