fd-find is simple:

    fd --type file --jobs 10 --execute my_script.sh {}

GNU Parallel can keep track of failures and help you re-run:

    fd --type file > files.txt
    parallel --joblog jobs.log --shuf --resume-failed --timeout 800% my_script.sh {} < files.txt
