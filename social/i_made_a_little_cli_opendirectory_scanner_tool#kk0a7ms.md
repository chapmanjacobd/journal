> without downloading it completely

Yes! ffprobe supports this out of the box actually. So it's as simple as passing the URL to ffprobe

exifTool also supports it kinda but not as well. I have to read the first 32KB of each http image and pass that data via temp file to exifTool. It could probably do with just the first 16KiB or even the first 8KiB for most files but it's only a little bit more to be safe

> A «baby project» , are you kidding us 

Well I mean the subcommand web-add specifically. I don't plan on replicating all the functionality that ODScanner or other tools might provide. But thank you! It's always nice to feel appreciated

> use datasette with the same way as Calishot

Yes it should work with datasette
