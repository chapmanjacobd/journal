You could use a browser addon like Copy Selected Links, go through each page, ctrl-a, Copy Selected Links, paste into a text editor, sort all the lines in the text editor, remove the non-video URLs, save as a file then do `yt-dlp -a file.txt` (or [cb](https://old.reddit.com/r/fishshell/comments/1655b4e/cb_clipboard_tool/))

There is probably a userscript to automate this https://www.tampermonkey.net/scripts.php?locale=en but be careful about self-XSS
