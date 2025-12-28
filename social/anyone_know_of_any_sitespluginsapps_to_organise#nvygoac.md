edit: Tartube looks like a good fit https://tartube.sourceforge.io/

You could make a spreadsheet via yt-dlp by choosing the attributes that you care about:

    pip install yt-dlp
    yt-dlp --flat-playlist --skip-download --print "%(title)q,%(uploader)q,%(duration)s,%(original_url)q" [URL] >> list.csv

I wrote a program that will create a SQLite database, it's pretty opinionated and might not get all the metadata that you want, but I personally use it to track over 20k+ YouTube, Vimeo, and other site playlists. yt-dlp supports all of these and even RSS feeds.

    pip install library
    library tubeadd my_playlists.db [URL]

Then you could use something like DBeaver or [datasette](https://datasette.io/tutorials/explore) to query the database and create new tables.
