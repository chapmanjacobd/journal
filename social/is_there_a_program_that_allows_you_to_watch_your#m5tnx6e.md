I wrote a program that can do that but it doesn't have a GUI and some of the options are not very intuitive:

Setup:

    pip install library
    library fsadd --video ./video.db /mnt/d/videos/

I usually do something like this:

    library watch ./video.db --local-media-only --random -o each -O

`-o each` will fetch the first folder sorted sibling. `-O` uses `natsort` to sort the playlist before playing. You can also use `-o all` to watch a whole randomly-selected season, for example
