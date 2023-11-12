You might actually be able to get the video from the Internet Archive:

    yt-dlp https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/$video_id

For example, this fish shell script:

    for base in https://youtu.be/ http://youtu.be/ http://youtube.com/watch?v= https://youtube.com/watch?v= https://m.youtube.com/watch?v= http://www.youtube.com/watch?v= https://www.youtube.com/watch?v=
        sqlite3 video.db "
            update or ignore media
                set path = replace(path, '$base', 'https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/')
                , time_deleted = 0
            where time_deleted > 0
            and (path = webpath or path not in (select webpath from media))
            and path like '$base%'
        "
    end
    # copied from https://github.com/chapmanjacobd/library#backfill-data
