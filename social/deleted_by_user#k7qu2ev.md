If you don't see the folders in your termux home directory you likely need to run termux-setup-storage

https://wiki.termux.com/wiki/Termux-setup-storage

And then you can create symlinks to make it easier. For example, on my Samsumg phone it looks like this:

    ln -s /sdcard/ ~/sdcard
    ln -s /storage/83gl-tg89/ ~/ext

`ls` the storage folder so you know what to replace `83gl-tg89` with
