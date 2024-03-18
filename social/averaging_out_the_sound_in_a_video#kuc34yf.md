If you use something like `mpv` you can run multiple audio filters to help with this without needing to write the audio out. For example...:

    _ af toggle "pan=stereo|FL=FC+0.30*FL+0.30*FLC+0.30*BL+0.30*SL+0.60*LFE|FR=FC+0.30*FR+0.30*FRC+0.30*BR+0.30*SR+0.60*LFE";show-text "Audio night-mode enabled"
    = af toggle "acompressor=ratio=4,loudnorm";show-text "dynamic range compression enabled"
    + af toggle "lavfi=[alimiter=10:1:1:5:8000]";show-text "Audio limiter enabled"

https://github.com/chapmanjacobd/computer/blob/main/.config/mpv/input.conf
