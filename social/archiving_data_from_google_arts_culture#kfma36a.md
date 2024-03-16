I made a tool to help scrape arbitrary links like this:

    $ pip install xklb
    $ lb links --selenium --manual \
      https://artsandculture.google.com/entity/m02y23 \
      --path-include /asset/

The browser will open and you'll need to click the right arrows on the Google Arts&Culture page to load beyond the first page. One could automate the clicking part with `xdotool`.

But if the page's javascript removes the links from the DOM as it loads more links you'll need to enter "y" into the "Extract HTML from browser? [y/n]" prompt between each browser click.
