I use it mostly to play music on all my chromecast speakers but it can do a lot more.

[https://github.com/chapmanjacobd/lb#readme](https://github.com/chapmanjacobd/lb#readme)

Basically:

    pip install xklb
    lb extract tv.db ./video/folder/
    wt tv.db

The default sorting is `play_count, duration / size` so it will prioritize files which are large. If you're not into that do:

    wt tv.db -u random

for a bit of entropy
