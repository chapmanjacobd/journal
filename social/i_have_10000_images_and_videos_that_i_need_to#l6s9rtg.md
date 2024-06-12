For a big project of any kind, the most important rule is incrementalism. You won't be able to finish all the work in a single day so you need to chunk it up into manageable pieces. 

To make starting/stopping work efficient it helps to have an index or log to keep track of which files you've sorted. This could be as simple as the file system where you have a file tree for unsorted data and another one for sorted data. I've been using [this](https://github.com/chapmanjacobd/computer/blob/main/bin/mktree.py) for about six months and it work okay. It feels very organized but I recommend minimizing the number of "tasks" folders. I think four is the right number. Five is almost too much.

You could also use spreadsheets or line-delimited file lists. That can work really well. I've done stuff before where moving lines between files was a really nice way to keep track of configuration. I even made a fish function to make it part of interactive tasks: [mvl.fish](https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/mvl.fish)

> mainly chrome bookmarks

For URLs specifically, I used to keep track of them in line-delimited files and that works really well. You can check the files into `git` and open ten at a time. This script will do that and delete the lines after they are opened: [openlinks.fish](https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/openlinks.fish)

I made a python CLI app that has a bunch of utilities for incrementally sorting different types of media. If you install it `pip install xklb` you can organize similar URLs together with this: `library cluster-sort bookmarks.txt sorted_bookmarks.txt`. That will organize the URLs not just by domain but also similar paths and words in the middle of the lines. It doesn't use AI but it is pretty spooky how well it works compared to more traditional tools like `sort --unique` but it is a bit slower, maybe 40 seconds for 100,000 lines.
