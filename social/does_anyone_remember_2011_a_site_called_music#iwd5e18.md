This site is pretty popular: https://everynoise.com/

If you have a list of favorite bands and want to listen to their old music which streaming services might not promote due to the long-tail effect, you could scrape all the songs into a database and play on shuffle to remove some of that personalized recommendation system bias. I made a program to do that but its a CLI:

    pip install xklb
    lb tubeadd music.db https://www.youtube.com/c/soundsofthedawn/videos
    lb listen music.db
