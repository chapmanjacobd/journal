It might help you understand how it works if you manually mount disks a few times. 

`mount` takes a block storage device from `/dev/*` and allows you to access the filesystem of the block device under a given path (for example `/mnt/usb/`). 

You can't easily directly access the filesystem from the block device--normally you would mount it first
