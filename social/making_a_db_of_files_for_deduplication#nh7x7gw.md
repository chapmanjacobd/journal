`rmlint` is fast! You usually don't need to do a full hash of all the data to deduplicate. I also wrote my own [de-duping script](https://github.com/chapmanjacobd/library?tab=readme-ov-file#dedupe-media). You could build off of that if you have specific needs.

But if you just want to search across filenames `plocate` is the right tool for the job. I use [this script](https://github.com/chapmanjacobd/computer/blob/main/bin/locate_remote_mv.py) to search across multiple computers which have plocate indexes updated. It's the same idea as voidtools' "Everything" but for Linux
