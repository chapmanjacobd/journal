1. I'd like to bind \e\[99\;6u (ctrl+shift+c) to copy the current commandline to the clipboard.

edit: this one was pretty easy actually...:

    function copy_to_clipboard
        commandline | head -c -1 | fish_clipboard_copy
    end

    bind \e\[99\;6u copy_to_clipboard

2.I'd like to bind \e/ (alt+/) to get the previous commandline in the current session and insert it to where the cursor is. 

For example:

    $ test 123
    $ echo ()

When the cursor is inside the parenthesis and alt+/ is pressed then the result will look like:

    $ test 123
    $ echo (test 123)

I tried `bind \e/ 'commandline -f up-line'` but nothing happened...

edit: this works but I don't know if it is the best way (specifically global history vs current shell session)

    function insert_previous_command
        commandline --insert -- (history -1)
    end

    bind \e/ insert_previous_command
