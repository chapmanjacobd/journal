You can store lists of files as lines of text then run this to do k-means clustering on similar words:

    pip install xklb
    lb cluster-sort file_paths.txt


        echo 'red apple
        broccoli
        yellow
        green
        orange apple
        red apple' | library cluster-sort --print-groups

        [
            {'grouped_paths': ['orange apple', 'red apple', 'red apple']},
            {'grouped_paths': ['broccoli', 'green', 'yellow']}
        ]

Also be sure to try `lb similar-files -h` `lb similar-folders -h`. You can scan once with `lb fsadd --fs disks.db` and pipe the list of files to all these commands; for example:

        $ lb fs audio.db --cols path,duration,size,time_deleted --to-json | lb similar-files --from-json -v
