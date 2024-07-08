> But I do have a file that passes and trying to understand why.

In ffmpeg 6+ I don't think `ffmpeg -v error ... -f null -` and checking the exit code is a viable way of finding errors. It's much better to use either `ffmpeg -report -i input.mkv -f null -` and parse or read that manually to determine if the error is something that you care about.

Are you just searching files for corruption? I've found that decoding frames and comparing (num_decoded_frames*frame_rate) with the duration metadata to be a relatively fast way of accurately finding corrupted or broken files. I found a similar method for checking audio too. More info here: https://github.com/qarmin/czkawka/discussions/721#discussioncomment-7944891
