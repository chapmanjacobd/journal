> some of the reencoded vids are larger than the original

Yes, I noticed this too. There are some tools out there to do automated video quality analysis, like this https://github.com/Netflix/vmaf but I haven't tried using them on a lot of files.

In the past I put together a script that reads the output of czkawka and helps speed up comparing two files by opening them side by side in mpv and then when you close the lower quality one it will delete it and open the next group of duplicates. But I haven't used it in a few months and I think it might need to be updated to work with the latest version of czkawka: https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/dedupe_czkawka.py

To use it install czkawka: https://github.com/qarmin/czkawka/releases

    czkawka video -d ./videos/ -d ./other_videos/ > video_dupes

then you can use the output file `video_dupes` like this:

    pip install xklb
    lb dedupe_czkawka video_dupes

All the options:

    lb dedupe_czkawka -h
    usage: lb [-h] [--auto-select-min-ratio AUTO_SELECT_MIN_RATIO] [--start START] [--volume VOLUME] [--gui] [--auto-seek] [--all-keep] [--all-left] [--all-right] [--all-delete] [--verbose] file_path

    Choose which duplicate to keep by opening both side-by-side

    positional arguments:
      file_path             Path to the text file containing the file list.

    options:
      -h, --help            show this help message and exit
      --auto-select-min-ratio AUTO_SELECT_MIN_RATIO
                            Automatically select largest file if files have similar basenames. A sane value is in the range of 0.7~0.9
      --start START
      --volume VOLUME
      --gui
      --auto-seek
      --all-keep
      --all-left
      --all-right
      --all-delete
      --verbose, -v
