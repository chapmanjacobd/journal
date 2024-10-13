~~So, I don't know if this will work but it might be worth a try~~

EDIT: I just tried it with a Google Takeout link and Google doesn't like it. It sends a `302` and redirects back to the manage downloads page. But it works most of the time on other sites so I'll leave this up:

~~If it does work you also need to consider (5.3 terabytes) / (15 MBps) = ~4 days so you might also need to use multiple IPs; but I don't know if Google limits based on account or IP address.~~

I wrote a script that reuses the yt-dlp code for loading cookies from your browser. You can use it like this:

    pip install xklb
    library download --fs --cookies-from-browser firefox temp.db URL1

Replace "firefox" with "chrome" if you use chrome

If it works with one URL you can use [rush](https://github.com/shenwei356/rush) (if you are on Windows) or GNU Parallel (use with --joblog so you can know if any failed--but you also can check temp.db with anything that can read SQLite) to process the full list of URLs.
