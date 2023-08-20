For size of dir I recommend `ncdu`

  


For deleting in parallel you could use GNU Parallel

    #!/bin/bash
    printf 'rm "%s"\n' "$@" | parallel

or with background jobs

    #!/bin/bash
    for item in "$@"; do /bin/rm $item &; done
    wait
