I think you can use this: https://github.com/sharkdp/fd?tab=readme-ov-file#on-windows

    choco install fd
    fd -tf -eOGG -eOPUS -eWAV -x ffmpeg -v quiet -stats -i {} {.}.mp3
