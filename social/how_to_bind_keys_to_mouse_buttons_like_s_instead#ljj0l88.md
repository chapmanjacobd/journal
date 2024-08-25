screenshot is just a command. It can take in other options like "MBTN_BACK screenshot video"

    s screenshot video   # take a screenshot of the video in its original resolution without subtitles
    ctrl+s screenshot window  # take a screenshot of the window with OSD and subtitles
    shift+s screenshot video each-frame

It might help to refer to the default config: https://github.com/mpv-player/mpv/blob/92f052c14e994b7ea77dc370b01bed5f8ef546db/etc/input.conf#L140

These are the default mouse settings:


    MBTN_LEFT     ignore              # don't do anything
    MBTN_LEFT_DBL cycle fullscreen    # toggle fullscreen
    MBTN_RIGHT    cycle pause         # toggle pause/playback mode
    MBTN_BACK     playlist-prev       # skip to the previous file
    MBTN_FORWARD  playlist-next       # skip to the next file

    # Mouse wheels, touchpad or other input devices that have axes
    # if the input devices supports precise scrolling it will also scale the
    # numeric value accordingly
    WHEEL_UP      add volume 2
    WHEEL_DOWN    add volume -2
    WHEEL_LEFT    seek -10         # seek 10 seconds backward
    WHEEL_RIGHT   seek 10          # seek 10 seconds forward
