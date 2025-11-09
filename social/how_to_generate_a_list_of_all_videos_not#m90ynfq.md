Like this:

    yt-dlp --flat-playlist -O original_url channel-link > channel_urls.txt

Once you have the lists you can use `combine` from `moreutils` to subtracts lines from files:

    combine channel_urls.txt not all_playlists_video_urls.txt > videos_not_in_playlists.txt
    yt-dlp -a videos_not_in_playlists.txt
