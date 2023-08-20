> when I re-install the OS, I would like to just install the new OS over the old one and mount the 7200RPM partition and continue from where I left off from

Sure. I think the most important part in all this, aside from setting up drives correctly, is to have backups in case something goes wrong during install. It's also likely that you could install a new OS on a different subvolume so if something goes wrong you can just tell your UEFI to boot into a different grub, or boot into a different drive from grub. Check out `grub-btrfs`
