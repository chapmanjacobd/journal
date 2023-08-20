> --write-sub --sub-lang "en.*" --write-auto-sub

I've found that this sometimes does weird things and it will skip downloading subtitles if they are in a weird language tag like "English (Great-Britain)" :/

On my machine just doing 

> --write-sub --write-auto-sub

did the "right thing" (of course this is subjective) whether a video had weird language tag, or whether the video only had autosubs or only normal subs or both.

but I don't know if yt-dlp just chooses English by default or if it looks up locale that the computer is running
