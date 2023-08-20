You can add more than one for sequential download--just put a space between:

    yt-dlp URL1 URL2 URL3

There is also [squid-dl](https://github.com/swolegoal/squid-dl) which seems pretty popular

If you want to download many videos but are often offline or have inconsistent internet access I wrote something that might help: https://github.com/chapmanjacobd/library 

`lb tubeadd` does a first fast pass at channels, playlists, or other URLs and saves the record in a SQLITE database. After that you can download `lb download` or stream directly to a video player which supports it one video URL at a time `lb watch`. You can open up multiple copies of `lb download` and they will check the SQLITE database in WAL mode to see if other processes already downloaded the video
