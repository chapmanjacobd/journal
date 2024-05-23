> --sub-langs "en"

I would recommend not setting this explicitly, unless it is not downloading the language that you want. There are many videos where this will cause subtitles to not be downloaded. ie. "en-GB" will not match, etc

> --write-auto-subs / --embed-auto-subs

Likewise, I think you can just use `--embed-subs` and it will get the "auto-subs" only if normal subs aren't available. You can test it out like this to verify:

    yt-dlp --skip-download https://www.youtube.com/watch?v=BaW_jenozKc --print requested_subtitles --embed-subs

### If you don't like sidecar files:

> --write-subs

I would recommend embedding the subtitles so that everything is in one file. Use `--embed-subs` instead. `--embed-subs --compat-options no-keep-subs` will even delete the subtitle files after it embeds.

> --write-description

`--embed-metadata` includes the description so you don't really need it as a separate file. You can use `ffprobe` to read it

My config:

Skip short videos, long videos, and live videos (`?` is needed because some extractors don't supply duration or live status)

    --match-filter "duration >? 59 & duration <? 14399 & live_status=?not_live"
