It's not really clear to me what you are trying to do but I will share a few things which might be useful:

### repeat a function (until it exits nonzero)

    function repeat
        while $argv
            and :
        end
    end

    function repeatslowly
        while $argv
            and sleep 1.5
        end
    end

    function repeatn --description 'repeatn <count> <command>'
        for i in (seq 1 $argv[1])
            eval $argv[2..-1]
        end
    end

### in the background

    function b
        fish -c (string join -- ' ' (string escape -- $argv)) &
    end

### you can combine these

    b repeatn 5 echo hello

If the above is helpful you might also like `until` which will repeat a command that is exiting nonzero _until_ it exits zero. If it exits zero the first time then it will only run once (no repeats):

    function until
        while not fish -c (string join -- ' ' (string escape -- $argv))
            and :
        end
    end


> actual instance of a function inside my session, that can access variables, call other functions and interact with my session

You might be looking for this:

    function x --no-scope-shadowing

Example here: https://stackoverflow.com/a/77384808/697964


For something hourly rather than interactive I would opt for systemd or cron. I have a fish function called `hourly` that I trigger with `fish -c hourly` via systemd-timer. It's very convenient because I can edit the function and it will run the updated function the next time the timer is triggered....
