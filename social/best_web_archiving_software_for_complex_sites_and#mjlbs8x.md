DiskerNet - https://github.com/dosyago/dn

WebScrapBook - https://github.com/danny0838/webscrapbook

wget2 - https://github.com/rockdaboot/wget2 (mostly limited to simple sites but it is often much faster than wget)

selenium-wire is deprecated but it still works pretty well at intercepting loaded assets (AJAX, etc)! I wrote some tools that use it which could be handy in a pinch: https://github.com/chapmanjacobd/library/blob/main/library/createdb/site_add.py

I also have a few other subcommands which support either real browser or cookies ~~but unfortunately not both~~. selenium doesn't have an easy way to load applicable cookies before loading a page. The requests python package makes it easy to load cookies but not puppet a browser... kinda sux

edit: [I took another stab at it](https://github.com/chapmanjacobd/library/commit/ea7e1cd30587744a413eb38e9b82f0d154fffa56) and it is working pretty well. You can now pass in `--cookies-from-browser` similar to yt-dlp and load them in selenium. You can also use `--user-data-dir` to reference the location of your browser config so you don't need to install browser extensions separately (however, Firefox doesn't like multiple sessions of the same profile open at the same time so you'll get an error if you already have your profile open when running the commands--so you may need to cp your profile first or use --cookies-from-browser instead)
