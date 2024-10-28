> I am not scared to make my own scripts in Bash

This isn't a WebUI but `yt-dlp --download-archive` works great.

I wrote [my own script](https://github.com/chapmanjacobd/library/) which extends the concept a bit: it will reduce the frequency of checks for channels or playlists that aren't updated frequently and it will increase check frequency when it finds that there are new videos for those URLs.

But really, all you need is what is built-in to yt-dlp. Realistically, this only make a difference when you have tens of thousands of subscriptions
