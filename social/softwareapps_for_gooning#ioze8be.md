I added experimental multiple playback support. I have only tested it on linux but it should work on Windows as well:

    pip install --upgrade xklb

    Playback multiple files at once
    library watch --multiple-playback   # default one per display; or two if only one display detected
    library watch --multiple-playback 4 # play four media at once, divide by available screens
    library watch -m 4 --screen-name eDP # play four media at once on specific screen

there is no limit other than crashing your computer:

    library watch --multiple-playback 9001  # it's over 9000!!!!111
