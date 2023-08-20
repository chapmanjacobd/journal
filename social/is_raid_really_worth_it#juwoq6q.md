The way that I use mergerfs is like this:

    /mnt/d/Videos/1.mkv
    /mnt/d/Videos/2.mkv

Then on the actual drives the data looks like

    /mnt/d0/Videos/1.mkv
    /mnt/d1/Videos/2.mkv

In my case files are evenly distributed across disks (but there are a lot of different mergerfs options and it is pretty configurable--if you prefer to keep subpaths together there are options to do so). 

If one disk goes down it means I miss some episodes of a TV show but I don't lose the whole TV show folder. Obviously whether that is preferred or not is subjective. I like it but I agree my setup is unusual perhaps even maniacal. The main reason why it's not confusing to me whether I watched something and deleted it vs it was lost is because I track that too: https://github.com/chapmanjacobd/library

I backup the metadata on the /mnt/d{0,9} mountpoints--not directly on the mergerfs overlay. This way I know what is lost
