I do this with mergerfs, btrfs reflinks, and this python script:

https://github.com/chapmanjacobd/computer/blob/main/bin/stickysync_local

Across network I have a similar script but you end up with duplicate space until you delete the local copy:

https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/stickysync_backup.fish 

(the main difference between this and normal rsync is that this won't copy files again after you delete or rename the files)
