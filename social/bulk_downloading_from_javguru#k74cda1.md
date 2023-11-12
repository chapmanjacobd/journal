You can try this which works for many javguru videos but it is still pretty slow and it will be limited by CPU but it _is_ automated:

    pip install xklb pyvirtualdisplay selenium  # it also requires ffmpeg and firefox
    cat javguru_video_links | parallel -j5 --joblog joblog_javguru --resume-failed python -m xklb.scratch.javguru {}

javtiful is a lot faster to download from and it has better encoding anyway. You can follow the above steps just replace javguru with javtiful and it will work.

Here are also a couple fish functions for automating video link extraction from javtiful:

    function javtiful_links --argument query total
        set last_page (math -s 0 "1+($total/23)")
        echo 'https://javtiful.com/'$query'&page='(seq 1 $last_page) | string split ' ' | parallel library links {} --include /video/ | tee /dev/tty >>~/.jobs/javtiful_misc
    end

    function javtiful_search --argument query total
        javtiful_links 'search/sort=newest/videos?search_query='$query $total
    end

    $ javtiful_search foreign 30

I don't plan on making changes to any of the above referenced code so don't open any tickets for the code inside the scratch folder but Pull Requests might be merged
