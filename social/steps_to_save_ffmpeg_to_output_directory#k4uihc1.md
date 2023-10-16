the last argument of an ffmpeg command is output.

So if you want to save to a different folder than the current working directory you just `mkdir -p my_fold3r/mysubfolder` if it doesn't already exist, and then type `my_fold3r/mysubfolder/my_file.mkv` as the last ffmpeg positional argument 

http://trac.ffmpeg.org/wiki/Creating%20multiple%20outputs
