If you're handy with the command line I've used my `library` tool on Android (via Termux) with some success. Here's an example:

    $ pip install library
    $ library webadd --audio test.db https://unli.xyz/audio/
    Pages to scan 0 link scan: 9 new [0 known]⏎

    $ library media test.db -pa
    path         count  duration              avg_duration                  size    avg_size
    ---------  -------  --------------------  ------------------------  --------  ----------
    Aggregate        9  1 hour and 0 minutes  8 minutes and 34 seconds  87.4 MiB    12.5 MiB

    $ ls yt_dlp/Generic/NA/
    Permissions Size User    Date Modified Git Name
    .rw-------   10M u0_a371 24 Nov  2019   -N 'Shouting Monkeys_NA_[Shouting Monkeys].mp3'

    $ library download test.db -s monk --prefix ./yt_dlp/ -v
    library v3.0.036 :: /data/data/com.termux/files/usr/bin
    ['/data/data/com.termux/files/usr/bin/library', 'download', 'test.db', '-s', 'monk', '--prefix', './yt_dlp/', '-v']
    {'include': ['monk'], 'prefix': './yt_dlp/', 'paths': []}
    [https://unli.xyz/audio/Shouting%20Monkeys.mp3]: Unrecoverable error matched. [download] Shouting Monkeys: Shouting Monkeys has already been recorded in the archive
    
You can remove the `-v` for less verbosity and you can use multiple webadd profiles at the same time, for example: `library webadd --audio --video --image` if you are interested in additional metadata for all those media types

The default mode of `library download` uses yt-dlp under the hood. To switch to gallery-dl you could use the `library download --image` flag. To switch to simple http downloading use `library download --fs`

Also, it's pretty easy to run `sshd` on Termux so you could use DownThemAll on desktop and then ssh into your phone to easily copy and paste lists of URLs and then download via `aria2c` or `axel`; or just email the lists to yourself; or copy your download lists via USB-MTP, etc
