maybe you could `dd` the drive and then:

    btrfstune -u /dev/sdX
    growpart /dev/sdX 1
    # mount it
    btrfs fs resize max /mounted
