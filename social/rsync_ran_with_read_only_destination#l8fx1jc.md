I'm not sure how Unraid works but I imagine that "Unassigned Disk" is a setting that is internal to Unraid rather than something like a bind mount:

    /mnt/disk1 /mnt/disk1ro none bind,ro 0 0
