> yt-dlp archive file

Yes, ideally you'd keep using the same file. I have an archive file that is over 1GB and it works fine:

    $ wc -l .local/share/yt_archive.txt
    50505260 .local/share/yt_archive.txt

Beyond a certain size you'll probably want to keep the download-archive file on SSD instead of rotating storage.

I even sync it using syncthing across computers and regularly de-dupe lines for conflict files:

    cat ~/.local/share/yt_archive.txt ~/.local/share/yt_archive.sync-conflict* | unique | sponge ~/.local/share/yt_archive.txt

[unique](https://gitlab.com/hydrargyrum/attic/-/blob/master/uniq-unsorted/uniq-unsorted.py?ref_type=heads), [sponge](https://rentes.github.io/unix/utilities/2015/07/27/moreutils-package/#sponge)
