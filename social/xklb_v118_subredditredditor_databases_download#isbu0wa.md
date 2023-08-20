for example one can now do:

    pip install --upgrade xklb
    lb redditadd reddit_music.db https://old.reddit.com/r/classicalmusic/
    lb download reddit_music.db --audio

Then run daily to get the newest posts

    lb redditupdate reddit_music.db
    lb download reddit_music.db --audio
