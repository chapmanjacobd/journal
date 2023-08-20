The program that I wrote should be able to handle this situation. If you try it and it doesn't work I'll fix it so that it does. It should work on both Windows and Linux

Initial scan:

    $ pip install xklb
    $ lb fsadd --filesystem -db school.db ./WS22-23

Searching via fts

    $ lb fs -db school.db -s KW46 L04 notes
    # this should open your default pdf reader with the file named "AMSP_WS2022_CH2_L04_Exercise_notes.pdf"

because it uses fts indexes it should be pretty fast even if your filesystem is large

If you just want to see a list of files then you can do

    $ lb fs -db school.db -s KW46 -p   # prints a table by default
    $ lb fs -db school.db -s KW46 -p f  # prints only filenames, good for piping to other programs

`lb fs -db school.db` is kinda long to type so I would do this if you use fish shell:

    $ abbr school 'lb fs -db school.db -s'

### Additionally, if you wanted to create a `text` database. This will also copy the text from within the files into the database:

    $ lb fsadd --text text.db ~/d/50_eBooks/

Then you could search for specific topics:

    $ lb fs -db text.db -s graduate-level programs -p

there is even some ocr functionality but I have not tested it and I don't personally use it because it is a bit slow. You may be better off with using something like Calibre at a certain point

    $ lb fsadd --text --ocr text.db ~/d/50_eBooks/

If you find this is useful, I should make sure that the `lb fs` subcommand only searches filesystem fts columns and the `lb read` subcommand searches all fts columns... I'm not sure if I have written that part in code but it would be easy to add
