It might be worth finding a GUI that provides generic functionality like [DropIt](http://www.dropitproject.com/) and then add a custom "Open With" action that will run something like this:

    ffmpeg "-nostdin -i %File% -movflags use_metadata_tags -c:a copy -map_metadata 0 .\audio\%FileName%.m4a"

https://dropitblog.wordpress.com/2011/11/14/line-up-with-command-line/

Using `-c:a copy` will be the fastest but [you'll need to make sure the output file extension matches](https://superuser.com/a/1594582/76968). 

If you don't have uniform inputs then it will be easier if you pick something specific to end up with like PCM `.wav` and when doing so you would use `-map 0:a` instead of `-c:a copy`
