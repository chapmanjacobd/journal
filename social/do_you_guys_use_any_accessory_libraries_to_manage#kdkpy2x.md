I've done some things which I feel are somewhat novel -- the code might be interesting to read. Not that the code is anything spectacular but that my approach to solving some of this problems might be interesting:

### library siteadd -- [site_extract.py](https://github.com/chapmanjacobd/library/blob/main/xklb/site_extract.py), [utils/web.py](https://github.com/chapmanjacobd/library/blob/main/xklb/utils/web.py)

Extract data from website requests to a database (right now only supports JSON, but I want to add protobufs, websockets, etc)

    library siteadd jobs.st.db --poke https://hk.jobsdb.com/hk/search-jobs/python/

### library eda -- [eda.py](https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/eda.py), [utils/file_utils.py](https://github.com/chapmanjacobd/library/blob/main/xklb/utils/file_utils.py)

Perform Exploratory Data Analysis (EDA) on one or more files. This works for http, gcs, aws s3 links too. If you need ftp I can probably add it--or maybe it already works but I haven't tested it.

Only 20,000 rows per file are loaded for performance purposes. Set `--end-row inf` to read all the rows and/or run out of RAM.

### library extract-links -- [extract_links.py](https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/mining/extract_links.py)

Extract links from within local HTML fragments, files, or remote pages; filtering on link text and nearby plain-text

    library links https://en.wikipedia.org/wiki/List_of_bacon_dishes --path-include https://en.wikipedia.org/wiki/ --after-include famous
    https://en.wikipedia.org/wiki/Omelette

Read from local clipboard and filter out links based on nearby plain text:

    library links --local-html (cb -t text/html | psub) --after-exclude paranormal spooky horror podcast tech fantasy supernatural lecture sport
    # note: the equivalent BASH-ism is <(xclip -selection clipboard -t text/html)

Run with `-vv` to see the browser

I haven't used these but they seem useful:

- https://github.com/alirezamika/autoscraper
