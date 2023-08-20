It's not 100% clear what you are trying to do so I'll just provide some generic guidance for how I use tmux:

You can connect to the same tmux session on multiple devices:

on pc:

    tmux new-session -A -s phone

from phone:

    ssh pc -t tmux new-session -A -s phone

If you want a separate session for something else just use a different name instead of "phone"

Spend an hour or two tinkering with the settings. It's worth it

https://github.com/chapmanjacobd/computer/blob/main/.config/tmux/tmux.conf

Also, you can try autossh with tmux instead of mosh

    autossh pc -t tmux new-session -A -s phone

https://hunden.linuxkompis.se/2019/03/10/automatically-reconnect-to-lost-ssh-connection.html
