you can have YouTube-dl save metadata to a SQLITE database. I've done this before for a different project. I'll share some code

I'm not sure of any GUI built for this but there is a GUI for SQLITE

edit: this might help... if you eventually find a GUI let me know because that might be interesting for me as well


    # you can run this file like this python save_yt_metadata.py https://youtube.com/c/DWDocumentary/videos/

    import sys
    import youtube_dl
    from db import insert_pg
    from rich import print
    import json

    ydl_opts = {"ignoreerrors": True, "quiet": True}

    youtube_dl.utils.std_headers[
        "User-Agent"
    ] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"

    for playlist in sys.argv[1].split(","):

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:

            playlist_dict = ydl.extract_info(playlist, download=False)

            if playlist_dict.get("entries") is None:
                playlist_dict = dict(entries=[playlist_dict])

            for video in playlist_dict["entries"]:
                if not video:
                    print("ERROR: Unable to get info. Continuing...")
                    continue

                row = dict(
                    upload_date=video.get("upload_date"),
                    uploader_id=video.get("uploader_id"),
                    track=video.get("track"),
                    id=video.get("id"),
                    title=video.get("title"),
                    description=video.get("description"),
                    duration=video.get("duration"),
                    age_limit=video.get("age_limit"),
                    view_count=video.get("view_count"),
                    average_rating=video.get("average_rating"),
                    categories=json.dumps(video.get("categories")),
                    tags=json.dumps(video.get("tags")),
                    subtitles=json.dumps(video.get("subtitles")),
                )

                print(video.get("uploader_id"))
                insert_pg("videos_ytchannels", row)
