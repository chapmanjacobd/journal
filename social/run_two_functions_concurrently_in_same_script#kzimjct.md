does this work for you?

    function b
        fish -c (string join -- ' ' (string escape -- $argv)) &
    end

You use it like this:

    b concurrent_thing 1
    b program2 --plus arguments
