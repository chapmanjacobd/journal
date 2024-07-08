> My other solution is not using cron and I will start yt-dlp manually but repeat the 200 channels in a text file 100 times so xarg will cycle through the 20000 channels running 24/7

This seems a bit excessive to me but to each their own... I subscribe to over 10,000 channels so it takes a while to check them all.

In my own scripts I added a delay for channels that are rarely updated. If there are no new videos since last time it will delay for twice as long as before, up to one year. If there are new videos then it will delay half as long as last delay. This way channels that are frequently updated are checked more often and channels which are rarely updated aren't checked too often: https://github.com/chapmanjacobd/library
