I think cbird was designed for this: https://github.com/scrubbbbs/cbird

> Image view: difference image can align to template match

The interface takes a bit to figure out.

    $ cbird -i.algos 1 -update
    $ cbird -dups -select-result -sort-rev resolution -chop -nuke  # delete exact duplicates
    $ cbird -p.dht 1 -similar -sort-rev resolution  # similar photos GUI

You could also use ImageMagick: https://imagemagick.org/Usage/compare/#difference

I like VisiPics but it is Windows only and it doesn't have anything to show the differences but it might be good for first pass dedupe
