I have a little over 2 million songs as well and I wrote [my own](https://github.com/chapmanjacobd/library) media management system to deal with it all. I save everything as Opus so the size is relatively small but still high-quality.

    $ library listen ~/lb/audio.db -pa
    ╒═══════════╤═════════╤═════════════════╤════════════════╤═════════╤════════════╕
    │ path      │   count │ duration        │ avg_duration   │ size    │ avg_size   │
    ╞═══════════╪═════════╪═════════════════╪════════════════╪═════════╪════════════╡
    │ Aggregate │ 2303944 │ 62 years, 3     │ 14.22 minutes  │ 12.6 TB │ 5.5 MB     │
    │           │         │ months, 27 days │                │         │            │
    │           │         │ and 19 hours    │                │         │            │
    ╘═══════════╧═════════╧═════════════════╧════════════════╧═════════╧════════════╛

Recently, I've automated a lot of it so every day I will automatically download songs that were posted to subreddits or YouTube channels which I follow (via [lb redditupdate](https://github.com/chapmanjacobd/computer/blob/a5108021ac1f2e320c9e01d26d086f3d513bfa69/.config/fish/functions/daily.fish#L19) and [lb tubeupdate](https://github.com/chapmanjacobd/library#1a-get-new-videos-for-saved-playlists)).

To find new music I searched reddit for music recommendations of different countries. I deduplicated and randomized that list (I saved a copy here: https://unli.xyz/music.txt). Every day 7 lines of that file are opened into Firefox tabs and if I like the music I'll add the channel to my auto-download list (via [lb tubeadd](https://github.com/chapmanjacobd/library#1-download-metadata)).

I use rsync to [move 400 random songs](https://github.com/chapmanjacobd/computer/blob/a5108021ac1f2e320c9e01d26d086f3d513bfa69/.config/fish/functions/mrmusic.fish#L1) every week to a folder which is shared (via syncthing) between my desktop, laptop, and phone. I can also mount all the music via sshfs but haven't found the need to do that unless I want to listen to something specific.

About 10 years ago I used Subsonic/Madsonic but with large libraries it takes a long time to rescan and it just seems kinda slow. So I run my own program (lb) on my phone (via Termux), laptop, and desktop. I set up keyboard shortcuts to start playing, stop playing, and to skip/delete the song.

When I skip a track I also delete it (via `lb next --delete`). Even when in the car or listening on the go ([Media Key Next](https://old.reddit.com/r/termux/comments/10h5j56/im_new_to_termux_so_suggest_me_what_cool_stuff_to/j57f9a8/?context=3) via Termux:tasker). Every few months or so if I've deleted a lot of music from that subfolder then I'll check that subfolder specifically and delete the whole folder if it contains music I don't like (via `lb bigdirs audio.db --sort-by-deleted`).

Every week I [backup](https://github.com/chapmanjacobd/computer/blob/a5108021ac1f2e320c9e01d26d086f3d513bfa69/.config/fish/functions/dbackups.fish#L14) songs that I've listened to and not skipped/deleted. Same with other media that I've watched and liked. I like being in that crate-digging mode so it doesn't bother me that I'm rarely listening to songs that are familiar. But a few times a month I do like listening to specific artists or genres.
