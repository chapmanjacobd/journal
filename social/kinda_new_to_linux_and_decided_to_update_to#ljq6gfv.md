If you have the time this is a great chance to learn how the different programs fit together: systemd, X11, sddm, kwin, plasmashell. 

Otherwise I'd boot up a Fedora USB and copy over your files to another disk (if you didn't make `/home` a separate partition) and then do a clean install


Try running `startx` or `startplasmacompositor`. If the desktop shows up then you can try installing `sddm` and make sure runlevel 5 is set. You might need to install x11 if Fedora 40 didn't keep it
