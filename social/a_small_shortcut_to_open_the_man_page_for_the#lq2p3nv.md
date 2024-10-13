Interesting! I think these shortcuts are better suited for the shell to manage. (Fish shell will open the man page with alt-h by default). But you helped me learn something today with that fancy `(echo (cat))` although I think you can rewrite it like this?

    man $(awk '/./{line=$0} END{print line}' | cut -d ' ' -f 2)
