ahh yeah I've had this happen before a few times. It's still an issue in fish-master `ae7b4010`. It is annoying but I'm not sure how difficult it would be to fix this, it might not be worth the effort ? I opened a ticket for you here: https://github.com/fish-shell/fish-shell/issues/10805

When this happens you can press `alt-e` to open the command in your `$EDITOR`. Or press `ctrl-x` to copy the command to your clipboard again:

    bind | grep -i fish_clip
    bind --preset ctrl-x fish_clipboard_copy

looks like it happens when pasting something that is one line or more longer than the window: 

`commandline --insert -- (seq 1 100)`

`seq 1 100 | fish_clipboard_copy; fish_clipboard_paste`

It's worth noting that other shells struggle with this too. In sh and bash when pasting the excess lines turn into [reverse video](https://en.wikipedia.org/wiki/Reverse_video) and the cursor is unable to move
