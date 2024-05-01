You might try getting the location of the iframe and passing that URL to other software but that won't work if the server wants a specific referrer, etc.

If you care about CSS, JS:

    wget --adjust-extension -e robots=off -np -nc -r -l inf -p --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64)" $URL

If the site is an index of links to media:

    $ pip install xklb
    $ lb webadd --selenium site.db $URL

This can scrape from iframes, even with postMessage or ShadowDOM, but it won't download on its own. It will create a list of links which can be downloaded via `lb dl site.db --fs` or passing to aria2, etc

If the site requires cookies you can pass them in like yt-dlp (but this doesn't work in selenium mode):

    $ lb webadd --cookies-from-browser firefox site.db $URL

If it doesn't work send me the site and I'll take a look.
