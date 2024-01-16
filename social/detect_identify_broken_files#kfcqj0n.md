I put together a script that does this recently. Here is some info:

1. Counting packets is likely the fastest way but not all formats use 1 frame per packet and so the resulting number is difficult to compare against.

1. The next slowest way is to copy the audio into a new container (like .mkv). This provides an accurate way to calculate how much of the file is missing because the duration of the new file will be different from the corrupt file.

1. The next slowest way is to count frames with ffprobe, similar to counting packets

1. Similar to option 3 is to decode only some frames instead of all frames. This is less accurate but much faster than decoding everything. Even with a small number of samples you can get a good idea of whether the file is corrupt or not.
 
1. The slowest but most accurate way is to decode the full file:

        ffmpeg -nostats -report -i input.mkv -f null /dev/null

    But it's difficult to automate parsing the resulting log because it is full of specific details.

I wrapped the above 1-4 options in the media-check subcommand here:

    $ pip install xklb
    $ library media-check -h
    usage: library media-check [--chunk-size SECONDS] [--gap SECONDS OR 0.0-1.0*DURATION] [--delete-corrupt >0-100] [--full-scan] [--audio-scan] PATH ...

Defaults to decode 0.5 second per 10% of each file

    library media-check ./video.mp4

Decode all the frames of each file to evaluate how corrupt it is (very slow; about 150 seconds for an hour-long file)

    library media-check --full-scan ./video.mp4

Decode all the packets of each file to evaluate how corrupt it is (about one second of each file but only accurate for formats where 1 packet == 1 frame)

    library media-check --full-scan --gap 0 ./video.mp4

Decode all audio of each file to evaluate how corrupt it is (about four seconds per file)

    library media-check --full-scan --audio ./video.mp4

Decode at least one frame at the start and end of each file to evaluate how corrupt it is (takes about one second per file)

    library media-check --chunk-size 0.05 --gap 0.999 ./video.mp4

Decode 3s every 5% of a file to evaluate how corrupt it is (takes about three seconds per file)

    library media-check --chunk-size 3 --gap 0.05 ./video.mp4

Delete the file if 20 percent or more of checks fail

    library media-check --delete-corrupt 20 ./video.mp4

To scan a large folder use `fsadd`. I recommend something like this two-stage approach:

    library fsadd --delete-unplayable --check-corrupt --chunk-size 0.05 tmp.db ./video ./folders
    library media-check (library fs tmp.db -w 'corruption>15' -pf) --full-scan --delete-corrupt 25

https://github.com/chapmanjacobd/library/blob/main/xklb/media/media_check.py
