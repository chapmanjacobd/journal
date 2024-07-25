To transcode you'll want something like this:

    ffmpeg -i input.mp4 -c:v libsvtav1 -preset 8 -crf 44 output.mkv

If you want a simple CLI tool that can take any video file and shrink the size and delete the original or transcode if it is bigger size:

    pip install xklb
    lb process-ffmpeg input.mp4

This will also convert animated gifs into AV1 files and non-animated gifs into AVIF files via imagemagick.

More advanced and time-consuming but higher quality:

- https://github.com/master-of-zen/Av1an
