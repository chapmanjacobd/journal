the ol'

    sudo DEBIAN_FRONTEND=noninteractive apt update -o APT::Update::Error-Mode=any && DEBIAN_FRONTEND=noninteractive apt upgrade -qq -y --allow-downgrades -o 'Dpkg::Options::=--force-confold' -o=Dpkg::Use-Pty=0

just kidding I am not insane

    sudo dnf install dnf-automatic
    sudo systemctl enable --now dnf-automatic-install.timer
