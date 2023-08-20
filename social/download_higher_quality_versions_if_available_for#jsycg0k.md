For YouTube it will be relatively straightforward to write a script that uses the download archive but for some other extractors (possibly including ESPN) the download-archive does not provide enough information to re-download a previously downloaded video (it only keeps enough info to prevent redownloading after a source URL is parsed).

If you want to do this, I recommend you start keeping track of source URLs somehow. At the very least be sure you are running yt-dlp with `--embed-metadata` so that you get the PURL embedded in the video or audio tags. 

In my TODO I'm tracking this as ["upscale" subcommand](https://github.com/chapmanjacobd/library/blob/main/TODO#L33) but that's probably a poor name. It's unlikely that I'll ever add an "AI upscaler" type functionality to my project but I should probably pick a better name. Maybe `video-upgrade`? If I can think of a good name maybe I'll start writing it this weekend
