wget2 https://github.com/rockdaboot/wget2

    wget --force-directories --adjust-extension --page-requisites -e robots=off -np -nc -r -l inf -p --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" --reject-regex '/tag/|/tags/|\?tag' --continue --tries=50 --dns-timeout=10 --connect-timeout=5 --read-timeout=45 --http2-request-window=15 --tcp-fastopen $URL

Sometimes you need to use `--retry-connrefused`, `--ignore-length`, or both. Sometimes you will _not_ be able to use `--tcp-fastopen`
