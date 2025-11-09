Generally, when pulling functionality from libraries, use of functions which start with "_" are discouraged.

I recommend taking a look at the source code to see examples of where _parse_html5_media_entries is called. It's likely that you'll need to run another function first which adds some information to the yt_dlp_instance.downloader object
