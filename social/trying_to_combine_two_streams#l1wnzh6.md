Depending how you're consuming the file, I think you'll want to have video as the first stream. This might be why you can't hear the audio or can't see the video?: 

>  The order of your -map options determines the order of the streams in the output. In this example the input file has audio as stream #0 and video as stream #1 (which is possible but unusual). Example to re-position video so it is listed first, followed by the audio: 

https://trac.ffmpeg.org/wiki/Map#Re-orderstreams

`-map 0:v -map 1:a`
