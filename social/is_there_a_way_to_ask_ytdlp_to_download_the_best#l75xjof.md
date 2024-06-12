If you only care about the final container:

    --merge mp4 --remux mp4

Those options will save to mp4 in a non-re-encoding way. But when mp4 [does not support](https://en.wikipedia.org/wiki/MP4_file_format#Data_streams) the codec streams it might still be saved as webm or mkv.

To force re-encoding "to mp4" (I guess this is usually x264) in those other cases, add this:

    --recode mp4
