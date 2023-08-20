> -mconvert=raid1c4 -dconvert=raid0

imho this doesn't make much sense. If you lose a drive then you effectively lose everything. `raid1c4` metadata doesn't provide any more realistic protection here than `raid1` metadata would. Switching to `raid1` metadata is my solution in the OP.

But since writting the OP I learned that, on a multi-disk btrfs device, `-dconvert=single` is not any better for data integrity than `-dconvert=raid0` so that part makes sense ([proof](https://gist.github.com/chapmanjacobd/bc6e31c8bc3647e0bcb0c43bc0464a9c#results)). 

If it's important to you to lose only some data rather than losing all data when one drive fails you would need to switch to something like mergerfs which I've done. The underlying fs that I use is still btrfs so I get the ability to know when bitrot occurs with `dup` metadata but I also get the media consumption/downloading continuity that I was looking for. It's a bit more complicated to set up but I feel performance overall is a faster than a large multi-disk btrfs--especially mounting time.

Here are some details if you are interested:

**You will need enough at least enough empty space as the size of your largest disk to switch over.**

- https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/mergerfs_add_disk.fish
- https://github.com/chapmanjacobd/computer/blob/main/.github/etc/fstab
- https://github.com/trapexit/mergerfs-tools/issues/39#issuecomment-1414592026
- https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/diskstatus.fish
