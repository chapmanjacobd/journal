You could try xmlstarlet: `xmlstarlet sel -t -v "//a/@href"` but it doesn't work for dynamically loaded content. I wrote this to extract links from such pages:

    pip install library
    library links https://URL1 https://URL2

If the links load via javascript then add `--firefox` or `--chrome` to load the page via selenium. If the page requires cookies then you can use `--cookies-from-browser` similar to yt-dlp. 

The `links` subcommand will print the links to stdout. The `linksdb` subcommand supports slightly more scenarios and saves links to a sqlite database. 

Most sites only require cookies or javascript--not both. However, if the page requires both javascript and cookies you'll need to use `linksdb` and login manually by doing something like this:

    library linksdb --max-pages 1 --firefox --confirm-ready URL.site.db https://URL1 https://URL2

For multiple pages you can try `--auto-pager` (with either `links` or `linksdb`) which works well on sites that either have a built-in infinite scroll or sites that are supported by weAutoPagerize; but if that doesn't work use the `linksdb` subcommand for pagination:

    library linksdb --path-include /video/ --page-key offset --page-start 0 --page-step 50 --stop-pages-no-match 1 -vvvv --firefox --confirm-ready URL.site.db https://URL1

The /video/ links will be stored in the file `./URL.site.db`
