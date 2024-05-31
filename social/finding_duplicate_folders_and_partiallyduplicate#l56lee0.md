I wrote a [CLI command](https://github.com/chapmanjacobd/library) recently to help with this. You can filter subfolders based on similar name, size, file count, or any combination:

    lb similar-folders -h
    usage: library similar-folders PATH ...

    Find similar folders based on foldernames, similar size, and similar number of files

        $ library similar-folders ~/d/

        group /home/xk/d/dump/datasets/*vector          total_size    median_size      files
        ----------------------------------------------  ------------  -------------  -------
        /home/xk/d/dump/datasets/vector/output/         1.8 GiB       89.5 KiB          1980
        /home/xk/d/dump/datasets/vector/output2/        1.8 GiB       89.5 KiB          1979

    Find similar folders based on ONLY foldernames, using the full path

        $ library similar-folders --no-filter-sizes --no-filter-counts --full-path ~/d/

    Find similar folders based on ONLY number of files

        $ library similar-folders --no-filter-names --no-filter-sizes ~/d/

    Find similar folders based on ONLY median size

        $ library similar-folders --no-filter-names --no-filter-counts ~/d/

    Find similar folders based on ONLY total size

        $ library similar-folders --no-filter-names --no-filter-counts --total-size ~/d/

    Read paths from dbs

        $ lb fs audio.db --cols path,duration,size,time_deleted --to-json | lb similar-folders --from-json -v

    Print only paths

        $ library similar-folders ~/d/ -pf
        /home/xk/d/dump/datasets/vector/output/
        /home/xk/d/dump/datasets/vector/output2/
