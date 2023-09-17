This might be obvious to some but I'm often copy and pasting web links and file paths into and out of my shell. This is how I do it fast: https://github.com/niedzielski/cb

    $ yt-dlp (cb)

After copying a bunch of links this will download all the links without needing to create a temporary file or use process substitution via psub.

Okay that's pretty much it. It's simple but powerful. 

Line-delimited output from subshells get converted into separate cmd arguments.

edit:

One other trick that I do is I have this in my config.fish:

    bind \b backward-kill-bigword
    bind \e\[1\;5C forward-bigword
    bind \e\[1\;5D backward-bigword

These let you use Ctrl-backspace to delete full arguments--even if they are long, for example: URLs. And Ctrl-Left/Right arrow keys to go between arguments
