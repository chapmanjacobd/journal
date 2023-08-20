You could also use GNU Parallel:

    #!/bin/bash
    printf 'rm "%s"\n' "$@" | parallel

Or if you're looking for nested empty directories `bfs` is the only real option available:

    bfs -nohidden -type d -exec bfs -f {} -not -type d -exit 1 \; -prune -ok bfs -f {} -type d -delete \;

https://github.com/tavianator/bfs

To auto-confirm at 10.2 GiB/s, pipe from the `yes` command
