This sounds like it would be more of a fragmentation issue rather than balance. https://old.reddit.com/r/btrfs/comments/hfpot9/what_does_balance_actually_balance/

You shouldn't worry about balancing in this case though you may want to use https://github.com/kdave/btrfsmaintenance. 

You can optimize the blocks by defragmenting:

    sudo btrfs filesystem defragment -r .git .config .local
