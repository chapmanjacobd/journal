This doesn't report all the problems in my experience. At least with ffmpeg 6.0.0+.

You can use this to catch (almost) everything: 

    ffmpeg -nostdin -nostats -report -i "$file" -f null /dev/null

But it is very verbose... And it's difficult to automate parsing the resulting log because it is full of specific details.

I put together a script which tries a few hacky shortcuts to speed this up and make it a bit more interpret-able. Here are a few different methods I found:

1. Counting packets is likely the fastest way but not all formats use 1 frame per packet and so the resulting number is difficult to compare against.

2. The next slowest way is to count frames with ffprobe, similar to counting packets

3.  Less accurate and slower than options 1 and 2 is to decode some frames. Even with a small number of samples you can get a good idea of whether the file is corrupt or not.

4. A slower way is probably to copy the audio into a new container (like .mkv). FFMPEG will give the new file an accurate duration.

I wrapped the above 1-4 options in the media-check sub-command here: https://github.com/chapmanjacobd/library#file-subcommands
