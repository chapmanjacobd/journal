I wrote a CLI script for merging/extracting tables across different sqlite files that might help with this.

Unfortunately, it looks like there are some data dependencies for `moz_keywords` ie. I guess `place_id` refers to `moz_places` and `moz_places` has `origin_id` which likely refers to `moz_origins`? You'll also probably want `moz_bookmarks`

It may help to install something like dbeaver and look into this more deeply. The following should work for overwriting but I haven't checked for other side effects:

    pip install library
    cp other_profile/places.sqlite other_profile/places.sqlite.backup

    library mergedbs --replace --only-tables moz_keywords,moz_places,moz_origins,moz_bookmarks main_profile/places.sqlite other_profile/places.sqlite

There's probably a firefox extension to selectively sync between profiles and that would work better for bi-directional sync. The above command can work with bidirectional sync but only for tables that have no data dependencies (no foreign keys, etc)
