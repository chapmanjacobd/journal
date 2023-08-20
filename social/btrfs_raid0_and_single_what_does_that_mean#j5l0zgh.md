> Single means the data is on a single spindle

this is not true. it means 1gb blocks are _allocated_ per drive but [a file's extents will still, more often than not, span multiple disks](https://gist.github.com/chapmanjacobd/bc6e31c8bc3647e0bcb0c43bc0464a9c#results).
