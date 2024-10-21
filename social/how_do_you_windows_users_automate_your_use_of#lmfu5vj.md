nushell runs on WIndows and it's a pretty good unix-like environment.

If you do something like:

    scoop install clipboard

or

    scoop install pasteboard  # replace cb with pbpaste below or add this script to your path: https://github.com/chapmanjacobd/computer/blob/main/.github/Windows/cb.bat

Then you can copy links and run 

    yt-dlp (cb)

without needing to paste the URLs directly.

In nushell, if you enable 

            name: history_menu
            only_buffer_difference: true

After you run it once then you can type `ctrl+r` yt or yt `ctrl+r` and then you don't need to type the rest--just press enter
