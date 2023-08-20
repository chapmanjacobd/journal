Firstly, if you have Fedora cloned across 2 nvme drives on the same machine you might consider wiping one of those drives then adding it as a btrfs raid1 drive:

    sudo wipefs -a /dev/nvme0nXpX
    sudo btrfs device add /dev/nvme0nXpX /    
    sudo btrfs balance start -mconvert=raid1 / 
    sudo btrfs balance start -dconvert=raid1 / 

If they are on separate machines, or for offsite backup purposes, I would recommend creating a setup script of Fedora, [like this](https://github.com/chapmanjacobd/dotfiles/blob/master/setup-fedora.sh) then rsync your home folder to an external drive: 

    # old disk
    rsync -auh --info=progress2 --no-inc-recursive ~/ /run/media/xk/backup/xk/

After installing fedora on your new computer then you would copy your backup folder back into your new home directory. When you reboot everything should just work.

    # new disk
    rsync -ah --info=progress2 --no-inc-recursive /run/media/xk/backup/xk/ ~/

if you have two computers you can also use syncthing on your ~/.local/ and ~/.config/ folders to keep most of your settings synced. It works surprisingly seamlessly. The only issue I've had are sync-conflicts for fish shell history so I have to concat the files back into the non-sync-conflict file--just be sure to use .stignore:

    $ cat ~/.config/.stignore
    /syncthing/**
    /borg/
    /yarn/
    /Code/
    /SideQuest/
    /chromium/
    /VSCodium/
    /Slack/
    /VSCode/
    /kwinrc

    $ cat ~/.local/.stignore 
    /state/
    /lib/
    /include/
    /share/Trash/
    /share/virtualenv/
    /share/virtualenvs/
    /share/containers/
    /share/icons/
    /share/DBeaverData/drivers/
    /share/kactivitymanagerd/
    /share/Steam
    /share/lutris
