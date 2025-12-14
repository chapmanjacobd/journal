awk is probably better suited but still... wish there was a shell builtin similar to `>>`... though it is a much more expensive operation! Prepending something requires rewriting the whole file :/

    awk 'BEGIN { print "#!/usr/bin/python3" } { print }' "$f" | sponge "$f"

Saving to the same file still requires `sponge`... `echo` and `cat` seem more lightweight in this scenario
