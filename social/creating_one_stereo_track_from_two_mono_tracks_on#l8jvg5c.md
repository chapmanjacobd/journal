I think it will be something like this:

    ffmpeg -i in.mp4 -c:v copy -filter_complex "[0:a:0][0:a:1]join=inputs=2:channel_layout=stereo[a]" out.mp4

- https://trac.ffmpeg.org/wiki/AudioChannelManipulation#a2monostereo
- https://trac.ffmpeg.org/wiki/Map

For batch processing on Linux/Mac I recommend GNU Parallel, example here: https://old.reddit.com/r/ffmpeg/comments/1chj4jp/take_first_40_frames_of_a_bunch_of_videos/l22ua4v/?context=3

For Windows I imagine that `fd-find` will work well: https://old.reddit.com/r/ffmpeg/comments/1db3dgr/split_videos_with_certain_aspects/l7on040/?context=3

Or use something like DropIt: https://old.reddit.com/r/ffmpeg/comments/1datmfk/gui_recommendations/l7mrdhu/?context=3
