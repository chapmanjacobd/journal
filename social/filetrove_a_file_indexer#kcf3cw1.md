well my tool is not really equivalent to this. I don't do hashes and I don't compare with NIST. Perhaps the only similarity is that I also use SQLite. 

My tool is focused on media and it has a few different scanning modes. It only uses exiftool with `fsadd --image`, ffprobe with either `fsadd --video` or `fsadd --audio`, and filetype via magic numbers using [puremagic](https://github.com/cdgriffith/puremagic/blob/master/puremagic/magic_data.json).

> link to your project

okay https://github.com/chapmanjacobd/library
