It's easiest to compare against the headers that your browser sends when retrieving the media file. If you open the Network Monitor in your browser you can keep adding headers until it works. But for more complex sites like Vimeo or YouTube you might need cookies too. At that point it is easier to use something like yt-dlp directly or passing to ffmpeg:

A command like

    pip install yt-dlp
    yt-dlp --downloader ffmpeg --skip-download --print-traffic https://www.dailymotion.com/video/x9bgdxu

Makes it really obvious what types of headers are being sent! 

If you are comfortable with line-breaks in your commands, you might find this syntax more intuitive: https://stackoverflow.com/a/78863381. If you are still confused maybe this site can help: https://www.jokecamp.com/blog/passing-http-headers-to-ffmpeg/

If you don't have `pip` or `pip3` but you have python or python3 then you can run this to install pip:

    python -m ensurepip

If you don't have python and are on Windows then I recommend installing [scoop](https://scoop.sh/) and then `scoop install python`
