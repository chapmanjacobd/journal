Thanks

    -    echo -n (commandline) | fish_clipboard_copy
    +    commandline | head -c -1 | fish_clipboard_copy

I agree that is nicer. I added the head to remove the last newline
