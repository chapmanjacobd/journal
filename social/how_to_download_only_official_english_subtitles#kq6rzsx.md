If you only use `--embed-subs` it should only download automatic captions if "real" captions don't exist. I'm not sure if it uses locale to determine the default language but in my case it defaulted to English.

You can run this to check which subs it will download if you still want to hardcode some subtitle language:

    yt-dlp --skip-download --print requested_subtitles $URL

should print "NA" by default

    yt-dlp --skip-download --embed-subs --print requested_subtitles $URL

this will print the subs that it will embed
