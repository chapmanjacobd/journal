AV1 is pretty sensitive to readahead and other buffers not being full. I've actually had it completely stall forever on minimal test videos where something like x264 never hangs.

So it's probably just waiting for IO to catch up or maybe it is a bug idk... but I've experienced what you are talking about too
