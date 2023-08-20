I think you are looking for this `=?`

    yt-dlp --match-filter "live_status=?was_live" "URL"

Should work on streamed and regular videos

If that doesn't work maybe you need 

    yt-dlp --match-filter "live_status=was_live" "URL" || yt-dlp --match-filter "live_status=?not_live" "URL"
