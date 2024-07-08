You can do a batch check of audio in video files with something like this:

    library fsadd audio_scan.db --check-corrupt --audio-scan --full-scan .\video\

Or for audio-only files (mp3, wav, etc)

    library fsadd --audio audio_scan.db --check-corrupt --audio-scan --full-scan .\audio\

Or to do a quick scan of video frames and only do a full video stream decode if more than 5% of frames fail

    library fsadd video_scan.db --check-corrupt --full-scan-if-corrupt '5%' .\video\

The amount of corruption will be saved to the SQLite file as a percent
