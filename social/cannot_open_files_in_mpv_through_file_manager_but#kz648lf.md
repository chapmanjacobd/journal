I would try

    sudo dnf reinstall mpv

Or manually add these in `~/.config/mimeapps.list` under Default Applications:

    application/x-partial-download=mpv.desktop;
    audio/mpeg=mpv.desktop;
    video/mp4=mpv.desktop;
    video/quicktime=mpv.desktop;
    video/webm=mpv.desktop;
    video/x-matroska=mpv.desktop;
    video/x-msvideo=mpv.desktop;
    application/x-partial-download=mpv.desktop;
    audio/mpeg=mpv.desktop;
    video/mp4=mpv.desktop;
    video/quicktime=mpv.desktop;
    video/webm=mpv.desktop;
    video/x-matroska=mpv.desktop;
    video/x-msvideo=mpv.desktop;
