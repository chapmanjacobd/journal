`mpv` already activates the correct track that I want but it would be nice if there was a lua script to toggle sub-visibility. I'm looking for the functionality of `subs-with-matching-audio` but I still want the subtitle to load so that another lua script, `sub-skip` will use it. Perhaps you can think of this as `sub-visibility=if-not-matching-audio`

In other words, when a video is first opened, and the activated subtitle matches the audio language track, I would like sub-visibility to be set to `no`.
