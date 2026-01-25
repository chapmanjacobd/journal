You might need to run this a few times a year when switching monitors or something but I've never had my audio driver crash _in the middle of a game_ just when starting one:

    systemctl --user restart pipewire-pulse.socket pipewire-pulse.service pipewire.service wireplumber.service

But the nice thing about linux is that you can bind this to a shortcut key so that if it ever happens at a critical time you just push a button to restart it instead of restarting the game
