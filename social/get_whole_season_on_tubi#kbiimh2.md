This gets the first 20 episodes of S15 but yeah you're right you'll need to write something custom or fix the Tubi extractor:

    $ pip install xklb
    $ lb links --scroll https://tubitv.com/series/300007764/pok-mon-the-series-black-white/season-15 --path-include /tv-shows/

edit: actually if you run the above with -vv and when the browser loads click to show the other episodes it should get all 50
