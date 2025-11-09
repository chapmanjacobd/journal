> I'm converting files that have huge bitrates ... to save space

Take a look at this python script, it will sort the files by estimated space saved before transcoding. It also supports image files, eBooks, and nested archives! But make sure to test it first to make it does what you want since it will delete stuff by default if the output file converted successfully!

https://github.com/chapmanjacobd/library/blob/main/library/mediafiles/process_media.py

This was inspired somewhat by https://nikkhokkho.sourceforge.io/?page=FileOptimizer

You can use it directly like this: 

    scoop install unar ffmpeg imagemagick calibre python fd
    pip install library

    library shrink processing/
    [processing/] Files: 639 [25 ignored] Folders: 49
    media_key      count  current_size    future_size    savings    processing_time
    -----------  -------  --------------  -------------  ---------  ------------------------
    Video: mp4       349  369.7GiB        104.9GiB       264.7GiB   7 days and 6 hours
    Video: mkv        99  85.3GiB         22.1GiB        63.2GiB    1 day and 13 hours
    Video: vob        23  13.7GiB         1.7GiB         12.0GiB    2 hours and 47 minutes
    Video: mov         6  2.8GiB          340.2MiB       2.4GiB     33 minutes
    Video: avi         6  2.7GiB          918.1MiB       1.8GiB     1 hour and 29 minutes
    Image: jpg       101  161.4MiB        3.0MiB         158.4MiB   2 minutes and 31 seconds
    Video: flv         1  397.4MiB        241.3MiB       156.0MiB   23 minutes
    
    Current size: 474.7GiB
    Estimated future size: 130.2GiB
    Estimated savings: 344.5GiB
    Estimated processing time: 9 days
    Proceed? [y/n] (n):

It will scan everything then ask you if you want to continue

If you don't like AV1, you could also use library to build a media database via the fsadd subcommand, then use something like `lb fs my.db -u bitrate -pf` to sort the files by bitrate and print only filenames
