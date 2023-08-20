Yeah... I tested removing 1 of 4 loop devices with about 80 GB of data total. Here are the results of my experiment: 

    Number of successful reads: 119
    Number of IO errors: 66

    Successful read files size: min 0       average 241136404 max 2397645276 sum 28695232117
    IO error files size:        min 1888612 average 745390515 max 4884066696 sum 49195774012

maybe I need to run a bigger test but the result of being able to read a 2.4GB file is probably somewhat surprising to the person who said only kbs would be accessible. But it is true that only 37% of data was still accessible, and this is a very small contrived simulation with only one process writing data.

It does seem like smaller files are going to be more likely to survive, but that can be expected. The gods of bits only make guillotines so big.

This result does make me feel a little bit better--though I will still investigate MergerFS a little bit more. I really like btrfs and switching to MergerFS seems like a lot of work...

A script to simulate this test using the output of `btrfs inspect-internal dump-tree --extents` might be interesting. I wonder how much file extent fragmentation my drives actually have.

https://gist.github.com/chapmanjacobd/bc6e31c8bc3647e0bcb0c43bc0464a9c#results

And I wonder if running btrfs balance would do anything to remove fragmentation or if it would make it worse. 

Is `btrfs filesystem defragment` related to extent fragmentation? If I ran that every month or two do you think that would improve the chance that a file would not be lost?
