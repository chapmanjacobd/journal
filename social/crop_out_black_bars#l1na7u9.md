> with 100% accuracy

If you have too many sources of video where you can't identify the crop that needs to happen from camera type and aspect ratio: it's safer to do cropping during playback.

For example, this works really well 90% of the time but 10% of the time it will use a black or partial frame and it will crop way too much. You can fix it in playback by toggling it again--but if an ffmpeg script did it you would need to re-transcode the whole video

https://github.com/chapmanjacobd/computer/blob/main/.config/mpv/scripts/easycrop.lua
