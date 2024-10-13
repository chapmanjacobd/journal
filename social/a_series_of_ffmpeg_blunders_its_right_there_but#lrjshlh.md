I would try installing ffmpeg via `scoop`. It doesn't require admin permissions and it should add itself to the `PATH` so yt-dlp should be able to find it after that

https://scoop.sh/

You could also use choco or winget but I recommend scoop due to its simplicity

yt-dlp also has a flag that you can use `--ffmpeg-location` but you'll need to specify that every time
