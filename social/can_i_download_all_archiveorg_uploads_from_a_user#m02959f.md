If the URL contains `/details/` then yt-dlp should be able to download everything linked within the resource. But for other URLs like searches, etc... I don't think those are supported yet. If jdownloader2 isn't working you can try this:

    $ pip install xklb
    $ library links --scroll "https://archive.org/search?query=creator..." --path-include /details/ > video_urls.txt
    $ yt-dlp -a video_urls.txt

Replace https://archive.org/search?query=creator... with the URL that you are looking at
