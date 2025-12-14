Now you can do something like this:

    echo AutomaticUpdatePolicy=apply | sudo tee -a /etc/rpm-ostreed.conf
    sudo rpm-ostree reload
    sudo systemctl edit --force --full rpm-ostreed-automatic.timer  # change to 3 days
    sudo systemctl enable rpm-ostreed-automatic.timer --now
    rpm-ostree status
