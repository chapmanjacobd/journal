I would likely use GNU Parallel. Have a list of streamers as a line-delimited text file, have your script which accepts a URL as the first arg (or use yt-dlp directly?). 

And then re-run every x mins? Maybe you need a simple lock file per URL. Here is how you could do that in fish shell:

    function create_lock_file
        set lockfile "/tmp/$argv.lock"
    
        if test -e $lockfile
            echo "Lock file $lockfile already exists."
            return 1
        else
            touch $lockfile
            return 0
        end
    end

    function clear_lock_file
        rm "/tmp/$argv.lock"
    end

Alternatively, you could create a sqlite file with timestamp of last checked and then have a script open yt-dlp as a daemonized process if there is a stream, but then you'll still need some kind of locking mechanism, probably using the `try: finally:` clause in python so you can clear locks on any errors.
