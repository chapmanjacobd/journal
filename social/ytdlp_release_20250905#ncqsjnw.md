Your problem might be better solved by using GNU Parallel with joblog and two passes of yt-dlp. The first time to turn playlists into video URLs:

    $ yt-dlp --flat-playlist -O original_url $playlist >> videos.txt

To prevent redownloads you'll want to remove duplicates when appending at a later time where unique is [something like this script](https://github.com/chapmanjacobd/computer/blob/main/bin/dedupe.py):

    $ cat videos.txt | unique | sponge videos.txt

Then pipe the videos.txt to your thumbnail downloading command:

    $ cat videos.txt | parallel -j 1 --joblog thumbnail_download_archive.log yt-dlp --write-thumbnail --skip-download -t sleep

(with GNU Parallel's `--resume-failed` you can retry failed ones)
