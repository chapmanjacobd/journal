They're both pretty good containers but converting between the two can lead to permanent metadata loss as some relatively common metadata fields and some relatively common subtitle formats aren't cross-supported (some are unique to MP4 and some are unique to MKV). 

MKV generally supports more codecs but there are even some video and audio codecs that are unique to MP4 (but mostly DRM or very obscure ones).

ffmpeg can _usually_ [convert between subtitle formats](https://github.com/chapmanjacobd/library/commit/559238944425017bb2d3e8c164c1e6d180d31ac6#diff-cc21bdd0155eaf44156fe4163d1dfa7bd9432b3d63c51fd6c0acdf3722942050) (ie. without which (if you use `-c:s copy`) you will get an error like "Subtitle codec 94213 is not supported" when converting from MP4 to MKV) but there will, very likely, be some metadata loss which may or may not change how the subtitles are formatted / displayed.
