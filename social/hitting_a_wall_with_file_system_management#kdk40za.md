If the concern is just speed of `rm`. an easy way to make it faster is to use GNU Parallel. Just delete files. Then you can use [bfs](https://github.com/tavianator/bfs) to efficiently clean up empty directory trees:

    yes | bfs -type d -exec bfs -f {} -not -type d -exit 1 \; -prune -ok bfs -f {} -type d -delete \;

But ideally you would use a filesystem feature which handles your retention and object lifecycle management concerns.
