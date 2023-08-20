like I said you need to check the manual. just google yt-dlp manual and when you're on that page you can ctrl-f "retries" but I don't recommend setting a higher number than 20 unless it's actually your internet connection's fault. If you keep hitting the same unavailable resource then YouTube will block your IP

Instead you should just rerun it multiple times with the --playlist-random flag using either one of these options:

[https://www.networkworld.com/article/3541298/how-to-repeat-a-linux-command-until-it-succeeds.html](https://www.networkworld.com/article/3541298/how-to-repeat-a-linux-command-until-it-succeeds.html)

or use gnu parallel with the retries flag
