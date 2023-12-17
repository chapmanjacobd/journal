You can use the exit code of this in an if statement to do something to the files that aren't `libx264`

    ffprobe -v error -select_streams v:0 -show_entries stream=codec_name \
      -of default=noprint_wrappers=1:nokey=1 "$video" | 
      grep libx264
