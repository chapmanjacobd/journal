> this is in preparation for adding two more 16TB drives and creating a raid1...

I think you can directly go from "any" state to your desired state. So what I imagine you should do is add the other devices, 

    sudo btrfs device add /dev/sdX /dev/sdY /mnt/X/

remove the usb device (if you have enough space) 

    sudo btrfs device remove /dev/sdX /mnt/X/

and then run balance with soft to resume the previous balance:

    sudo btrfs balance start -mconvert=raid1c3,soft /mnt/X
    sudo btrfs balance start -dconvert=raid1,soft /mnt/X

>  and full redundancy

This should be fine for 4~6 drives but know that btrfs raid1 can't handle more than one drive failure: https://gist.github.com/chapmanjacobd/bc6e31c8bc3647e0bcb0c43bc0464a9c#results. (If you ever want to safely expand your storage beyond this point you may need to copy out data from the filesystem one drive at a time unless you buy enough drives to copy it all in one go into a new storage system)
