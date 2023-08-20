ahh interesting. if it boots but it is read only I think it should still work and that would be easier than futzing around in a non GUI environment but if BusyBox has network access that shouldn't be too difficult either.

I'm not sure how to solve your btrfs problem but most likely you'll need a LiveUSB environment anyway. Most linux distributions provide a Live environment and it's as simple as

    dd if=Fedora.iso of=/dev/sdX
where sdX is the location of your USB. You can find it by running

    sudo fdisk -l

to mount a RAMdisk you'll need an empty folder that already exists somewhere... in a read-only environment idk what places you can use but once you find one replace /mnt with that folder

    mount -t tmpfs -o size=1G tmpfs /mnt/
