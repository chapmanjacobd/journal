I saw something recently that did this but for BASH:

https://github.com/chapmanjacobd/journal/commit/839da4f29d3b22ca25a9d9e2b6f9a83d82775b5d

It also might be worth mentioning that opening new panes in kitty terminal can open to the current directory. I think this will apply to `yazi` as well though you may need to set the title to be the cwd:

    map ctrl+shift+enter new_window_with_cwd
    map ctrl+shift+t new_tab_with_cwd !neighbor

(just an example, I'm sure other terminals support a similar thing)

> as well as for commands that yazi would send to its own subshell to run on the other shell

this seems very specific to the implementation of `yazi` and I'm not sure how you could get a generic solution to work without modifying the program's source code
