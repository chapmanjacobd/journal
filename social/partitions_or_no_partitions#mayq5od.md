If you do decide to do this and have a bunch of disks it's a good excuse to learn wipefs and sgdisk

    sudo wipefs -a /dev/sdX
    sudo sgdisk -n 0:0:0 -t 0:8300 /dev/sdX
    sudo partprobe
