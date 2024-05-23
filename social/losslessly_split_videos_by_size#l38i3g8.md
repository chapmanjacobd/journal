You can use the `-fs` parameter to limit size:

https://stackoverflow.com/questions/38259544/using-ffmpeg-to-split-video-files-by-size

To do it without re-encoding use `-c copy` and don't add specific encode options like `-c:v libx264` etc 

(edited)
