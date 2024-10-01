If it is indeed a list of segments to not include, maybe the only confusing thing is the infile and your example commands. If someone is not familiar with ffmpeg they might not think it is confusing but these seem to be opposite:

    file video.mp4
    inpoint 34.5
    outpoint 55.1
    file video.mp4
    inpoint 111.0
    outpoint 155.3
    file video.mp4
    inpoint 278
    outpoint 316.4

and 

    python ffmpeg_batch_cut.py -i video.mp4 -s 0:34-0:55 1:51-2:35 4:38-5:16 combined.mp4
