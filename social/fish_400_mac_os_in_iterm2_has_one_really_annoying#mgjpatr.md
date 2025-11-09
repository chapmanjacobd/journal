Are you sure it's different from before? `Option+.` should do what you want. You can use the bind command to compare fish 3.7 with 4.0:

    $ bind | grep -i alt-right

For example, these are the defaults I see:

    bind --preset alt-right nextd-or-forward-token
    bind --preset alt-left prevd-or-backward-token                              
    bind --preset alt-up history-token-search-backward
    bind --preset alt-down history-token-search-forward                         
    bind --preset alt-. history-token-search-backward

It sounds like you want

    bind alt-right history-token-search-backward

https://github.com/fish-shell/fish-shell/issues/10756
