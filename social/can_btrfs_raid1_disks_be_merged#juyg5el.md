You run btrfs on your phone??

Here is what I do for phone backups. It might not work for you but it has brought me a lot of peace of mind. I'm not worried if I lose my phone because I only lose up to one day of data:

I'm using Android but you could easily do something similar on a Linux phone. I have [cron set up via Termux](https://github.com/chapmanjacobd/phone/blob/main/setup.sh) to run [a script to copy/move files](https://github.com/chapmanjacobd/phone/blob/main/.shortcuts/tasks/syncthing.sh) into a syncthing folder [every night](https://github.com/chapmanjacobd/phone/blob/main/.jobs/crontab). The main reason why copying/moving is necessary is due to Android 13 folder security--but if you have an older version of Android or a Linux phone you could probably setup sync folders in syncthing for each folder that you want to backup instead.

I sync everything on my phone and I've never encountered any major problems with Syncthing-Fork. I can edit or move files around on my phone and it will update on my PC and vice-versa. It's very convenient
