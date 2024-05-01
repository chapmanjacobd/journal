modify your `--output` to include folder names:

ie.

    "%(ie_key,extractor_key,extractor)s/%(uploader,uploader_id)s/%(autonumber)s - %(title)s.%(ext)s"

Or you'll need to write a script that does something like this fish shell script:

    for bf in (fd -elist)
        set out_path (path dirname $bf)
        yt-dlp ... --paths $out_path ... --batch-file $bf
    end

https://github.com/sharkdp/fd
