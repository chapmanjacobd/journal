If you just need to check if the link is supported you could do this:


    def is_supported(url) -> bool:
        return any(ie.suitable(url) and ie.IE_NAME != "generic" for ie in yt_dlp.extractor.gen_extractors())

but the Generic extractor works wonders across many sites

Or maybe by validate you want `--check-formats` 

Or by events you want a hook: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#adding-logger-and-progress-hook ?
