If you're trying to download recursively from the Wayback Machine you generally don't get everything you want or you get too much. For me personally, I want a copy of all the sites files as close to a specific time-frame as possible--similar to what I would get if using `wget --recursive --no-parent` on the site at the time.

The main thing that prevents that is the darn-tootin' _TIMESTAMP_ in the URL. If you "manage" that information you can pretty easily run wget on the Wayback Machine.

I wrote a python script to do this here:

https://github.com/chapmanjacobd/computer/blob/main/bin/wayback_dl.py

It's a pretty simple script. You could likely write something similar yourself. The main thing that it needs to do is track when wget gives up on a URL because it traverses the parent but this could just be seconds or hours from the initial requested URL. Unfortunately, the difference in Wayback Machine scraping time leads to wget giving up on the URL because the timestamp in the parent path is different.

If you use wget without `--no-parent` then it will try to download all versions of all pages. This script only downloads versions of pages that is closest in time to the URL that you give it initially.
