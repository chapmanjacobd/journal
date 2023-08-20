I won't pretend to be a gooner but I am a data hoarder and I want to share some of the things that I've learned/created. 

For collection and curation of various media I wrote my own [CLI](https://github.com/chapmanjacobd/lb/).

    wt tax.db -p a -w 'play_count=0'
    ╒═══════════╤════════════╤════════╤═════════╕
    │ path      │ duration   │ size   │   count │
    ╞═══════════╪════════════╪════════╪═════════╡
    │ Aggregate │ 10 months, │ 3.8 TB │  223838 │
    │           │ 8 days, 9  │        │         │
    │           │ hours and  │        │         │
    │           │ 53 minutes │        │         │
    ╘═══════════╧════════════╧════════╧═════════╛

I haven't experimented with multiple-playback, but given the size of my catalogue I probably should at some point. My workflows are focused on curation. I keep around 8% of the things that I download.

For videos I curate with this:

    function relaxvid
        fish -c 'lb extract ~/lb/tax.db ~/d/60_Now_Watching/ ~/d/64_Relaxation/' &
        mpv --input-ipc-server=/tmp/mpv_socket --no-video --af="acompressor=ratio=4,loudnorm" (fd -eOPUS -eOGA . ~/d/64_Relaxation) &
        lb wt ~/lb/tax.db -L inf --action askkeep --keep-dir /home/xk/d/69_Videos_Keep/ --sort "path like '%64_Relaxation%' desc, time_modified, duration desc, priority"
        pkill -x mpv
    end

It will ask whether you want to keep the video after you close mpv or after the video goes to the end. If you press enter then it will delete the video. If you type `y` and enter then it will move the file to the `keep-dir`

For photos I use `feh`:

    function relax
        fish -c 'lb extract ~/lb/tax.db ~/d/60_Now_Watching/ ~/d/64_Relaxation/' &
        ~/d/64_Relaxation
        mpv --input-ipc-server=/tmp/mpv_socket --af="acompressor=ratio=4,loudnorm" (fd -eOPUS -eOGA . ~/d/64_Relaxation) &
        feh -q -F --hide-pointer --sort filename --on-last-slide resume --action2 "mv '%f' ./keep/" --action1 "trash-put '%f'" --action3 "mv '%f' ../95_Memes/" --action4 "mv '%f' ../96_Weird_History/" --action5 "mv '%f' ../52_Receipts/" --action7 "mv '%f' ../94_Cool/" --action8 "mv '%f' ../93_BG/" --action6 "mv '%f' ../98_Me/" --action "trash-put '%f'" -G --auto-zoom --zoom max --draw-tinted --image-bg black --scale-down -D -3 .
        pkill mpv
    end

Also, I highly recommend buying an adjustable bed. It's really a game-changer. Using that and something like [this](https://www.amazon.com/MagicHold-Rotating-Height-Adjusting-13-15-6/dp/B07NXZNC88) the experience is similar to those really expensive [zero gravity workstations](http://www.ergoquest.com/uploads/5/9/1/5/5915120/screen-shot-2020-06-21-at-8-11-23-am_orig.jpg). You could do the same with the Timber Ridge Zero Gravity Chair and some laptop or monitor stand for under $200.
