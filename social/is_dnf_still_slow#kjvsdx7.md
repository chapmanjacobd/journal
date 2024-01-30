Most likely the slowness that people perceive is latency like when searching for a package. The main factors that influence this are which mirrors are chosen and if dnf is doing a speedcheck to find the fastest mirror.

To solve this you could likely disable fastestmirror and hardcode a specific mirror that you like. However, I agree with some of the other people here. Better to leave the defaults and instead enable auto-update:

    sudo dnf install dnf-automatic
    sudo systemctl enable --now dnf-automatic-install.timer
