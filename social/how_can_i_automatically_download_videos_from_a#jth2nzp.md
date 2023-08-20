I have a [script that does it](https://github.com/chapmanjacobd/library#getting-started) but you'll need some way to run it every x interval. cron works well for this. What I do is have a `fish` shell function called daily then I set `fish -c daily` to run daily in `cron`. Whenever I want to add something to my daily script I just run `funced -s daily` and it is really easy. But you could just as easily accomplish the same thing in any shell by using a text file.

    library tubeupdate edu.db
    library download edu.db --video --prefix ~/Videos/YT/
