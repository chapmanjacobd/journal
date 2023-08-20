Search YouTube for videos of how to boot from USB

  


Recovery is usually done by backing up your data, installing an OS, then copying your files back. Usually the only thing you need to backup is your home folder. Basically like this, but be aware that when you are on LiveCD the ~ will point to the LiveCD's temporary home folder and not your mounted internal drive so replace ~/ with the absolute path to the home folder in your internal drive:

    # old disk
    rsync -auh --info=progress2 --no-inc-recursive ~/ /run/media/xk/backup/xk/

After installing the OS on your new computer then you would copy your backup folder back into your new home directory. When you reboot everything should just work.

    # new disk
    rsync -ah --info=progress2 --no-inc-recursive /run/media/xk/backup/xk/ ~/

Most linux USBs include a "LiveCD" which allows you to run the full linux operating system from your USB so you can mount your internal drive and copy your home folder from it onto another external drive. 

I advise you to keep that external drive as a backup anyway because external SSDs are so cheap nowadays your time is likely worth enough rather than configuring your system over and over. Most desktop configuration is stored in the .local or .config hidden folders of your $HOME directory (~/). But grub config is stored elsewhere and it's often easier to just reinstall the whole OS when that stuff breaks
