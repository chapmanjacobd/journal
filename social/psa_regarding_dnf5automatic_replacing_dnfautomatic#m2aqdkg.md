thx for this!

in other words

    echo '
    [commands]
    apply_updates = yes
    ' | sudo tee -a /etc/dnf/automatic.conf

    sudo systemctl enable --now dnf5-automatic.timer
