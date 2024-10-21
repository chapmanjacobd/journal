> rename the "-s" flag

I think that's fine as-is. 

> The infile and command using my tool in your comment do identical things

Do they though? I would think the generated infile would look like this:

    file video.mp4
    inpoint 0
    outpoint 34.5
    file video.mp4
    inpoint 0:55
    outpoint 1:51
    file video.mp4
    inpoint 2:35
    outpoint 4:38
    file video.mp4
    inpoint 5:16
    outpoint (video end)

(but in seconds if ffmpeg only supports seconds)
