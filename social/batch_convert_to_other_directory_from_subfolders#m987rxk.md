I would use fd-find for this

https://github.com/sharkdp/fd?tab=readme-ov-file#placeholder-syntax

I don't believe ffmpeg will make the folders for you so you need to run mkdir first:

    fd -eMKV . src/ -x mkdir -p dest/{//}

    fd -eMKV . src/ -j2 -x ffmpeg -i {} \
        -movflags use_metadata_tags \
        -c:v copy -c:a copy -c:s copy \
        -map_metadata 0 -map_chapters 0 dest/{.}.mp4

This will run 2 files in parallel. I normally use not more than 3 parallel ffmpeg jobs per CPU socket.
