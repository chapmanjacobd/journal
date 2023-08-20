I have over 30,000 tabs... I append to a text file what I couldn't read at the end of the month so my browser stays relatively snappy.

Then I have a few systemd timers which open tabs from the file (with sed to delete the same number of lines that it opened): 7 at 10am, and 14 at 5pm. That's all I can handle. It's been pretty good so far. I estimate I will reach tab zero in about 4 years.

In addition to that I also automate opening specific tabs for pages that I know will change often (subreddits, etc). That code is part of my media library: https://github.com/chapmanjacobd/lb/#start----tabs-visit-websites-on-a-schedule

edit: a couple days ago I added an option, `lb surf`, to load browser tabs in a streaming way (close a tab and another one from stdin opens in the background). It only works with firefox currently https://github.com/balta2ar/brotab/issues/87
