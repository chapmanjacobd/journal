If you came to this page to learn how to enable hibernation in Fedora the answer is likely not here. [Behold the holy book of Fedora hibernators](https://www.ctrl.blog/entry/fedora-hibernate.html)! Respect and enjoy the peace.


I have a Tuxedo Pulse 15 and I tried installing Fedora 35 Beta1.2 without CSM enabled but it would always get stuck booting up the install media with an error like this:

    xhci_hcd Timeout while waiting for setup device command
    usb 4-2: device not accepting address 2, error -62

So I tried enabling CSM I was able to install Fedora and it made my target disk with an MBR/BIOS grub (which I don't mind). 

Things have been working well with the exception of hibernation. 

I have another laptop which is a Lenovo Flex 5, same setup (it was able to install Fedora 35 Beta1.2 with EFI), and hibernation is working perfectly. So I'm thinking... hibernation doesn't work for non-EFI booting?

systemctl suspend works

    Oct 30 12:05:32 fedora kernel: PM: suspend entry (deep)
    Oct 30 12:05:47 fedora kernel: PM: suspend devices took 0.210 seconds
    Oct 30 12:05:47 fedora kernel: ACPI: PM: Preparing to enter system sleep state S3
    Oct 30 12:05:47 fedora kernel: ACPI: PM: Saving platform NVS memory
    Oct 30 12:05:47 fedora kernel: ACPI: PM: Low-level resume complete
    Oct 30 12:05:47 fedora kernel: ACPI: PM: Restoring platform NVS memory
    Oct 30 12:05:47 fedora kernel: ACPI: PM: Waking up from system sleep state S3
    Oct 30 12:05:47 fedora kernel: PM: resume devices took 0.799 seconds
    Oct 30 12:05:47 fedora kernel: PM: suspend exit

systemctl hibernate seems to work but when I boot it back up it doesn't resume the session

    Oct 30 12:05:59 fedora kernel: PM: Image not found (code -22)
    Oct 30 12:05:59 fedora kernel: PM: hibernation: hibernation entry
    Oct 30 12:06:31 fedora kernel: PM: hibernation: Registered nosave memory: [mem 0x00000000-0x00000fff]


    ~ 🃄 cat /proc/cmdline
    BOOT_IMAGE=(hd0,msdos1)/vmlinuz-5.14.14-300.fc35.x86_64 root=UUID=071803bd-1e01-4d19-a8ff-eded9b53508b ro rootflags=subvol=root rd.luks.uuid=luks-36490a89-e4ec-4be1-84f0-92c85699698b rhgb quiet resume=UUID=b1c4f91e-b3f3-4405-b458-7d935b8b1fb1

    [root@fedora xk]# cat /etc/fstab 
    UUID=b1c4f91e-b3f3-4405-b458-7d935b8b1fb1 none                    swap    defaults        0 0

    [root@fedora xk]# cat /etc/default/grub 
    GRUB_DEFAULT=saved
    GRUB_DISABLE_SUBMENU=true
    GRUB_CMDLINE_LINUX="rd.luks.uuid=luks-36490a89-e4ec-4be1-84f0-92c85699698b rhgb quiet resume=UUID=b1c4f91e-b3f3-4405-b458-7d935b8b1fb1 "
    GRUB_DISABLE_RECOVERY="true"
    GRUB_ENABLE_BLSCFG=true

    [root@fedora xk]# cat /etc/dracut.conf.d/resume.conf 
    zadd_dracutmodules+=" resume "



I'm kinda giving up at this point but it is kinda frustrating that it works fine on one laptop but not the other one. If anyone has any ideas I'm willing to try it.

EDIT: ooof... I just realized my dracut conf had an extra z in there. there should be a warning when running dracut -f.... let's see if this works...

EDIT2: okay yeah that fixed it. now I feel dumb but I'm happy it works
