tmux

    bind-key -T copy-mode C-Home send -X history-top
    bind-key -T copy-mode C-End  send -X history-bottom
    bind -T copy-mode C-Up send-keys -X previous-prompt
    bind -T copy-mode C-Down send-keys -X next-prompt

kitty

    map ctrl+up scroll_to_prompt -1
    map ctrl+down scroll_to_prompt 1
    map shift+PAGE_UP scroll_page_up
    map shift+PAGE_DOWN scroll_page_down

fish shell config.fish

    if test -z "$SSH_TTY"; and test -z "$TMUX"
        bind pageup "kitty @ scroll-window 1p-"
        bind pagedown "kitty @ scroll-window 1p"
    end
