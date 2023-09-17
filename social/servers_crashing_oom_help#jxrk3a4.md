Yes, earlyoom is so much more stable than systemd-oomd. I haven't had anything hang since switching on my desktop. Very simple to configure

    sudo nano /etc/default/earlyoom
    EARLYOOM_ARGS="-r 0 -m 6,4 --prefer '^(Web Content|Isolated Web Co)$' --avoid '^(dnf|packagekitd|systemd|systemd-logind|dbus-daemon|dbus-broker|cryptsetup|sshd)$'"
    sudo systemctl enable --now earlyoom
