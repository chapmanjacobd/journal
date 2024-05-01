pipe to GNU Parallel

    set joblog (mktemp)
    cat cids.txt | parallel --shuf --joblog $joblog ipfs pin add
    parallel --retry-failed --joblog $joblog -j2
