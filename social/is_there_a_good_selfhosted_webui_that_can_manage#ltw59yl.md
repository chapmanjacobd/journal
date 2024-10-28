The only caveat that I can think of is this: if YouTube doesn't have the resource available (eg. rate-limited category and/or subtitles not generated yet) but yt-dlp is still able to download _something_ then it will count that as a success and those subtitles will never be retried.

Luckily, the yt-dlp authors have made it [relatively easy](https://github.com/chapmanjacobd/library/blob/main/xklb/createdb/tube_backend.py#L553C1-L560C54) to override `--download-archive`, but I haven't seen many programs do so in practice. I think most people are fine with the defaults
