You can use mpv and xklb to organize files:

    pip install xklb
    lb fsadd 2003.db .\unsorted_videos\

This will read in all the video files from the folder into a sqlite database which you can reuse with various commands, such as:

    lb watch 2003.db --multiple-playback 4 --sort time_created desc --loop -i \
         --cmd5 'mv {} D:\Gold\' \
         --cmd6 'mv {} D:\Silver\'

Bind a key to `exit 5` in mpv `input.conf` and press that while the video is playing to move it to Gold, etc

If you want to preserve directory hierarchies use `lb relmv` instead of `mv`. Then something like `.\unsorted_videos\2023\04\22\video.mp4` will become `D:\Silver\unsorted_videos\2023\04\22\video.mp4` instead of `D:\Silver\video.mp4`
