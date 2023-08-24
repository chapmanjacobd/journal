I put together a data extract of HackerNews containing all the submitted playable URLs.

https://github.com/chapmanjacobd/hn_mining/raw/main/hackernews_only_direct.tw.db

You can keep track of which ones you've played via the `xklb` app:

    pip install xklb
    wget https://github.com/chapmanjacobd/hn_mining/raw/main/hackernews_only_direct.tw.db
    library watch hackernews_only_direct.tw.db --random --ignore-errors

mpv has first-class support but if you don't have mpv installed and have any issues with playback please open a ticket: [xklb / library app](https://github.com/chapmanjacobd/library)

[HN Data](https://github.com/chapmanjacobd/hn_mining#watch-hackernews-from-your-cli)

You can also do this to play in the background

    library listen hackernews_only_direct.tw.db

or to download small videos

    library download hackernews_only_direct.tw.db --prefix ~/Downloads/ --video --small -v 

I use linux but it should work on Windows and MacOS without needing any additional configuration
