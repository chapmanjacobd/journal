If the files already exist then it should skip over them--but a better way is to use `--download-archive audio.txt` then even if you delete the files yt-dlp will skip over them if they were already downloaded.

You can also use [xklb](https://github.com/chapmanjacobd/library) to keep track of websites which aren't supported by yt-dlp's download-archive (ie. sites that use the generic extractor). 

The other (small) benefit of this is that it prevents sending out unnecessary HTTP requests for duplicate links and it will check playlists less often when there are often no new videos [which can be helpful if you have many playlists (you can use `tubeupdate -f` to force updating all playlists)].
