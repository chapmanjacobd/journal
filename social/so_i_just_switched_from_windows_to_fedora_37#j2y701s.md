yeah you'll see something like this:

    $ sudo efibootmgr 
    BootCurrent: 0004
    Timeout: 1 seconds
    Boot0003* Fedora
    Boot0004* Windows Boot Manager

In that case run this:

    sudo efibootmgr -o 0003,0004

and then you could run this whenever you want to reboot into windows for one time without messing with UEFI:

    sudo efibootmgr -n 4
