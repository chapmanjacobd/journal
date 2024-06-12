Thanks for your thoughts. I agree `mv` is perfectly fine in most cases. 

It seems like most people use rsync when they discover that `mv` doesn't merge. It is often the highest upvoted answer in relevant Stack Overflow questions. Rsync is very capable but it doesn't rename local files. It always copies and then deletes. 

This tool is essentially the interface and behavior of Rsync but better for merges on the same filesystem because it can rename files (which Rsync doesn't do).

Previously, I wrote another tool that simulates file clobbering of multiple file tree merges before renaming any files. But it is a bit slow because it reads the whole destination tree first https://github.com/chapmanjacobd/library/blob/main/xklb/folders/merge_folders.py
