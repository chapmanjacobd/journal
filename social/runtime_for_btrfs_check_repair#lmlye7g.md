> Unsafe Shutdowns: 54

> I'm tempted to just re-install Mint and use ext4 and encrypt the whole disk instead

Unfortunately, there aren't many good "self-healing" utilities for btrfs. The `btrfs check` sometimes gives weird results which is why they only recommend running `--repair` after getting good output from `btrfs check` without `--repair`.

Once a btrfs mount has gone read-only, in my experience this usually means the drive is on the way out--regardless of what SMART says. This might sound extreme and I agree it is. In many ways btrfs is the ideal filesystem--but it is _too_ ideal, too good for this world. A _lot_ of hardware is shit. Bitflips can and do happen. Some drives handle static electricity and surges (eg. lightning storms) better than others.

Every time this happens to me (a few times a year) I always think btrfs sucks but then after testing the hardware it has _always_ been hardware that is the root cause of these failures.

By the time you have hardware errors pop up in the btrfs metadata (vs. btrfs data) it's likely that something is very wrong at the hardware level.

That being said.... you need to consider what you need in a filesystem. Btrfs is awesome that it helps detect these hardware errors as they happen--of course it is frustrating that hardware is not perfect and it is expensive to replace. If you are fine with some possible corruption in your data (ie. if you can [detect](https://serverfault.com/a/1153301/77768) / fix / replace it at the application layer) then I think ext4 is a fine choice. In $CURRENT_YEAR I wouldn't use ext4 for the system drive but that's just my opinion

To properly fix this you would want to test/replace your RAM and SSD--but it's also possible that the problem is in your mobo/CPU

You can try:

- sudo btrfs rescue zero-log /dev/sdX1
- sudo mount -o ro,rescue=all /mnt/X
- reboot

Sometimes that will allow you to mount `rw` but most of the time you'll be stuck with `ro` until you reformat the drive.
