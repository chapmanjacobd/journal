Hey /r/selfhosted

This project has been slowly simmering on the back-burner over the past three years under the name "xk library". There have been a number of unique features added over the years and I haven't spent much time promoting it. Recently, the name "library" was made available to me in PyPI so I've started publishing to that instead of the temporary package name "xklb".

I don't personally use *arr nor Plex/Emby/Jellyfin so there may be some overlap with those ecosystems/applications. I don't think I would be able to convince you to use my CLI suite _instead_ of those because it's really not a replacement for them (unless you are a hardcore CLI addict)--however, there are a few interesting subcommands, which I will highlight below:

Load cookies from firefox and download all the zip files linked on the page:

    library links --cookies-from-browser firefox --path-include .zip --download https://example.com/site/with/links

Download all the files linked within the HTML fragment in your clipboard except the ones with the URL text "preview":

    library links --text-exclude preview --download --no-extract <(library links --local-html $(xclip -selection clipboard -t text/html))

Play sixty-four videos in mpv at the same time:

    library fsadd ./video.db ./hot_wheels_tournament/
    library watch ./video.db -m 64

Sort similar lines (sentences) together

    library regex-sort ./3000_movie_reviews.txt ./3000_movie_reviews.sorted.txt

Most of the subcommands have a lot of options. Documentation can be found with -h or --help:

    library regex-sort -h | less -FSRXc

The documentation for this command is like 100 lines long so I'm not going to paste it here. But you can read through each command's help documentation online without needing to install it: https://github.com/chapmanjacobd/library?tab=readme-ov-file#regex-sort

Many of the features work on Windows but there are a few that are Linux/Mac OS specific and some that only work on Linux.
