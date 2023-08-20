I'm not planning on writing a program to scan and only restore missing extents (though that would be cool). The ideal situation for me with `single` mode would be that losing a drive means only losing 1x~2x drive capacity of data (4x would even be acceptable) I know this has more to do with probability than anything else so I'm not expecting an exact/even number.

The data that I'm storing can likely be redownloaded from YouTube (again, there is a certain probability that it would be deleted by the time that I tried to redownload it). The majority of the data is *likely* not worth the cost of storing it in redundancy, because I have no emotional connection to it yet so if half (or even 75%) of that data disappeared it wouldn't cause a fault in continuity for my media consumption.

The script I would write therefore would be pretty simple: catalog all the files which are IO errors, delete them, and match the file paths with an existing database to mark them for redownloading.

Your replies have been helpful. I have a very pedestrian understanding of how files are written to disk and I will do more research about blocks and extents. And I'll experiment to see how much data btrfs actually can recover. Maybe I should be using `raid0` if the end result of drive failure is the same lol :-)

edit: 

yeah... after running 

    sudo btrfs inspect-internal dump-tree --extents /dev/sda

I can start to see how fragmented all the files are...
