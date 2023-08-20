It depends where you want to source music from and what level of quality is acceptable for you.

I don't have access to a listening room so I feel that YouTube is usually good enough for me. YouTube offers Opus in webm format so no re-encoding is necessary to have everything in a consistent format (96kbps Opus is similar quality to 256kbps mp3 for *most* music). If you want the highest quality listening experience then of course you will want to use lossless formats (FLAC, ALAC) but that comes with higher file size. yt\-dlp also works with Bandcamp, many other sites, etc. 

I have a list of YouTube channels and playlists which I save as a text file then every day I schedule the command to run  

    yt-dlp -a list.txt --playlist-end 30 -f bestaudio --cookies-from-browser firefox -i \
        -o "%(uploader)s/%(title).100s [%(id)s].%(ext)s" --restrict-filenames \
        --download-archive ~/.local/share/yt_archive.txt --retries 13 --extractor-retries 13 \
        --reject-title "Trailer|Preview|Teaser|Promo|Live Stream|Crypto"

    # you can try with -f bestaudio[ext=webm] first which will be faster for youtube videos that support it 
    # but it won't usually work for other websites.

    # the --playlist-end 30 is there because if we are checking every day we don't want to keep checking the same hundreds of playlist pages, 
    # we only need to check the most recent one or --playlist-end 90 to check the latest 3 pages

    fd . -H -tf -eWEBM -j8 -x bash -c 'mkvextract "{}" tracks 0:"{.}".oga && rm "{}"'


I never like using Spotify or YouTube Music for streaming music so I have a [script](https://github.com/chapmanjacobd/lb) which uses \`catt\` to play from my music collection to my Google Home speaker group.

I usually only buy albums after I've listened to them a few times (or if I want to support the artist sometimes I will just donate money directly to the artist but not a lot of musicians' have donate buttons).

Downloading purchased music is more difficult to automate and I'm lazy so I always download those files manually or I don't bother downloading them (this might seem crazy-but if I already have the music then I don't usually need to bother with downloading it even after I already paid for it and even though it is likely higher quality--the main reason is that I often can't tell the difference. I've done several blind listening tests and I don't have nice enough speakers or nice enough ears to tell the difference
