> resizing the partitions to overcome faulty hardware

Due to the way SSDs work I don't think this will help. Theoretically but unlikely it could help to format ext4 with badblock check (mkfsext4 -c) but I'm pretty sure this won't help much -- especially because SSDs are not lile HDDs. Sector errors do not usually bubble up that far. It may help to have some unpartitioned space at the end of the drive though

> btrfs vs ext4 on system drive

If I had to choose only one: root folder. But if you have important documents in your home folder maybe that is a better choice for you. I still use ext4 but only for disks that are failing and I only store files on there that I can redownload from somewhere else.

> tools for verifying hardware

highly recommend reading this: https://www.mersenne.org/download/stress.txt

If you're not seeing any errors in btrfs device stats / then most likely the problem is in your RAM so I'd start there but the problem could still be your drive.

- memtest
- stress can test storage: https://web.archive.org/web/20190629131203/http://people.seas.harvard.edu/~apw/stress/FAQ
- https://askubuntu.com/a/460463/1145624
- https://superuser.com/questions/789303/how-to-monitor-btrfs-filesystem-raid-for-errors
- prime95 + https://github.com/fhoekstra/thread_switcher
