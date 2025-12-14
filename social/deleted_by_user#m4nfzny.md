ps. I think the `.mka` container will support more input audio codecs:

    ffmpeg -i input-video.webm -vn -acodec copy output-audio.mka

https://en.wikipedia.org/wiki/Comparison_of_video_container_formats#Audio_coding_formats_support

Looks like Matroska has support for more common codecs like WMA (partial support), PCM (WAV, AIFF) files that MPEG-4 doesn't have (but which might be in .mkv files). But MPEG-4 supports a few proprietary codecs like PPCM, DV Audio, and MPEG-4 specific patent encumbered audio formats (ALS, SLS) which might be in .mp4 files, etc
