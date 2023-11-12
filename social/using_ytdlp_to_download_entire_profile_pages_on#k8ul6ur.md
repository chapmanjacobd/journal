You can also use this free tool to extract links:

    $ pip install xklb
    $ yt-dlp $(
      lb links --scroll --auto-pager 'https://archive.org/search?query=creator%3A%22Kinji+Fukasaku%22' | 
      grep /details/
    )

For many results you should use process substitution: `yt-dlp -a <(lb links ...)` 

or save the output to a temporary intermediate file first: `lb links ... > file.txt`

(You can run with `lb links ... -vv` to see the browser that is running behind the scene)
