That can have a lot of false positives. https://github.com/chapmanjacobd/library/blob/main/library/mediafiles/media_check.py

The only check that is 100% useful to automate if you don't want to try swapping headers is to use ffprobe to check if it can read the metadata.
