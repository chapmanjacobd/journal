> confirm_os_window_close

Negative values are converted to positive ones, however, with shell_integration enabled, using negative values means windows sitting at a shell prompt are not counted, only windows where some command is currently running.

https://sw.kovidgoyal.net/kitty/conf/#opt-kitty.confirm_os_window_close

Also related:

Asks for confirmation before closing the window. If you don’t want the confirmation when the window is sitting at a shell prompt (requires Shell integration), use:

    map f1 close_window_with_confirmation ignore-shell

https://sw.kovidgoyal.net/kitty/actions/#action-close_window_with_confirmation
