Last updated 3 years ago. 

I've never had any problems with it. Maybe the only footgun, footnote to be aware of is task concurrency (ie.`BTRFS_ALLOW_CONCURRENCY`):

https://github.com/kdave/btrfsmaintenance/commit/93b00548b212604a491d47531f37534d7d10f0a2

I would recommend leaving that option `false`. It is the default at least in my distro.

You can likely install the script via your system package manager. For example:

    sudo dnf install btrfsmaintenance

Edit the file here:

    visudo /etc/sysconfig/btrfsmaintenance

you only really need to set these two:

    BTRFS_BALANCE_MOUNTPOINTS="auto"
    BTRFS_SCRUB_MOUNTPOINTS="auto"

And then 

    sudo systemctl start btrfsmaintenance-refresh
