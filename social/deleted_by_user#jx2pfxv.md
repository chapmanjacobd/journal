My tool library will use ffprobe and store chapter count as a column in SQLITE

https://github.com/chapmanjacobd/library

After scanning with `fsadd` you can do stuff like this:

### see how many files have at least one chapter

    $ library fs /tmp/t.db -w 'chapter_count>0' -pa
    path         count  duration                avg_duration      size    avg_size
    ---------  -------  ----------------------  --------------  ------  ----------
    Aggregate       12  4 hours and 44 minutes  24 minutes      2.5 GB    208.2 MB

### print the names of files that have zero chapters

    $ library fs /tmp/t.db -w 'chapter_count=0' -pf

### only watch videos which have chapters; play in alphanumeric order

    $ library watch /tmp/t.db -w 'chapter_count>0' -O

then use [Datasette](https://github.com/chapmanjacobd/library#datasette) or query the database directly
