I wrote something that should be pretty fast. It uses hashes of small segments of each file first then does a full SHA256 hash if any partial hash matches. It's 10 times faster than rmlint on my machine and my script is cross-platform:

- https://github.com/chapmanjacobd/library?tab=readme-ov-file#dedupe-media

Also for merging folders, I wrote `lb mv` recently which can do similar sample-hash collision check on file conflict if you use the `--replace-same-hash`. I also wrote `lb merge-folders` which can tell you how many path conflicts there are before moving any files but it doesn't have the sample-hash conflict check

`lb mv` has pretty good tests: https://github.com/chapmanjacobd/library/blob/main/tests/folders/test_merge_mv.py but since you are only merging folders be sure to run it with `--no-bsd` so that it is not confusing
