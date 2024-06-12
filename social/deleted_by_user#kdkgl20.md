It sounds like you are batching data processing--just a random thought:

It's possible to create filesystems as loopback devices. I don't have experience with this, I'm sure there are tradeoffs that need to be evaluated--like write speed and failure cases. But you might be able to use loopback devices as lightweight partitions to make deleting files faster... 

    truncate -s20G d1.img
    set ld1 (sudo losetup --show --find d1.img)
    sudo mkfs.btrfs "$ld1"
    sudo mkdir -p /mnt/loop1
    sudo mount "$ld1" /mnt/loop1

Then when you don't need a month of data you just unmount and delete:

    sudo umount /mnt/loop1
    sudo losetup -d "$ld1"
    rm d1.img
