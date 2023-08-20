Feh can do this:

    feh -q -F --hide-pointer --sort filename --on-last-slide resume --action2 "mv '%f' ./keep/" --action1 "trash-put '%f'" -G --auto-zoom --zoom max --draw-tinted --image-bg black --scale-down -D -3

when pressing 1 the file is trashed. when pressing 2 it moves to the keep subfolder
