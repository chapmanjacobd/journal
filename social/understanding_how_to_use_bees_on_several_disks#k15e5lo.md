What are Bees?? I have a feeling this doesn't have anything to do with btrfs.

You can create a btrfs filesystem as a file or partition:

    truncate -s20G d1.img
    set ld1 (sudo losetup --show --find d1.img)
    sudo mkfs.btrfs -d single -m dup "$ld1"
    sudo mkdir -p /mnt/loop
    sudo mount "$ld1" /mnt/loop

    sudo btrfs device usage /mnt/loop

    sudo umount /mnt/loop
    sudo losetup -d "$ld1"
    rm d1.img
