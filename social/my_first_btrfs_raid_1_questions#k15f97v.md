> move the two drives to another machine. Is it simple as plug it and run the software?

Yes. You just need to plug in one or both drives and it should mount with the same configuration as your previous machine. But if you have special mounting options in fstab you would need to copy them over, for example:

    defaults,users,noatime,nodiratime,compress-force=zstd:2,nofail,x-systemd.mount-timeout=999

You can get the UUID from lsblk:

    lsblk -io NAME,TYPE,SIZE,MOUNTPOINT,FSTYPE,MODEL,UUID
