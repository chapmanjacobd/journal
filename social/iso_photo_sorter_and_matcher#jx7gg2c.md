I think [czkawka](https://github.com/qarmin/czkawka) is the best option right now or maybe [cbird](https://github.com/scrubbbbs/cbird). 

For videos at least czkawka was faster to use for bulk scanning, though I had to write [my own script](https://github.com/chapmanjacobd/computer/blob/main/bin/czkawka_output_dupdelete.py) to facilitate comparing. The script works on photos too but it requires mpv


    $ czkawka image -d (pwd) > dupes.txt
    $ wget https://raw.githubusercontent.com/chapmanjacobd/computer/main/bin/czkawka_output_dupdelete.py
    $ python czkawka_output_dupdelete.py dupes.txt

cbird has a much more sophisticated UI but it struggles a bit if you have millions of photos.

    $ cbird -i.algos 1 -update
    $ cbird -dups -select-result -sort-rev resolution -chop -nuke  # exact duplicates
    $ cbird -p.dht 1 -similar -select-result -sort-rev resolution -chop -nuke  # similar photos

but if you are on Windows, and your collection isn't in the millions range I recommend VisiPics
