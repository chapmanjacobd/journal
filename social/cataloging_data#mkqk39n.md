plocate is one of the fastest that I've used. 

    sudo systemctl enable --now plocate-updatedb.timer

I wrote a script, [locate_remote_mv.py](https://github.com/chapmanjacobd/computer/blob/dda5323ed96de93eca5eb261aad2218a5863e3e2/bin/locate_remote_mv.py), to check a bunch of computers and move files I'm interested in. 

You could also use something like sshfs instead, but you may need to edit [/etc/updatedb.conf](https://github.com/chapmanjacobd/computer/blob/dda5323ed96de93eca5eb261aad2218a5863e3e2/.github/etc/updatedb.conf) to remove `fuse.sshfs` from PRUNE_FS to allow it. Also, if you use mergerfs be sure to add `fuse.mergerfs` to PRUNE_FS to block it (so you don't end up with duplicate entries)
