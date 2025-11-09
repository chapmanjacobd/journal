> but there is hundreds of projects and as far as i know there is no way to keep the file structure if i throw everything in one timeline

fd-find or GNU Parallel should be able to preserve your file structure, ie: fd -eMOV -j4 -x ffmpeg -i {} ... {.}.mp4

https://github.com/sharkdp/fd?tab=readme-ov-file#placeholder-syntax

But if you need the exact same output filenames as input filenames you'll want to script something that saves to a temporary file first and then replaces the existing file
