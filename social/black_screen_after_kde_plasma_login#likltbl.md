In case this is helpful for others... The reason for me was that I disabled activity monitor in Plasma 5. 

Plasma 6 does not like this!

    kde.plasmashell: Aborting shell load: The activity manager daemon (kactivitymanagerd) is not running.
    kde.plasmashell: If this Plasma has been installed into a custom prefix, verify that its D-Bus services dir is known to the system for the daemon to be activatable.

I had to undo what I did before:

    rm ~/.local/share/kactivitymanagerd
    sudo chmod +x /usr/libexec/kactivitymanagerd

Then I could run `plasmashell --replace` and it loaded the desktop instead of hanging
