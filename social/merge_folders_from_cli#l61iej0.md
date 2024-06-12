`mv` doesn't work well with folder conflicts. It raises an error if any subfolders match existing folders. It can't merge filetrees at all.

Here are some concrete examples: 

https://github.com/chapmanjacobd/journal/blob/main/programming/linux/misconceptions.md#when-the-destination-has-a-subfolder-with-the-same-name

Note also that `mv ./src/* ./dest/` does not solve the merge filetrees problem because `mv` will just put the conflicting folders as nested same-named subfolders

But you _could_ use some combination of `find`, `mkdir` and `mv` to solve this problem in a similar way to the script.

> add a disclaimer that the merge function seems to be a small part of a big library

Well the whole package is only a couple hundred KiB. But you are right I could make more of the dependencies optional like ffmpeg, etc.
