It's really just the DE but that includes many different default programs.

You could use the everything-netinst to do a minimal or server install and then add KDE and it is close to the same experience.

    # dnf groupinstall "KDE Plasma Workspaces"
    # systemctl set-default graphical.target
