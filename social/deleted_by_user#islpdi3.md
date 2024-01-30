> paranoid of programs creating random configuration files around my home directory

I used to be paranoid like this but it really is as simple as creating a git repo in your home directory, then running `git add .; and git reset --hard` when you notice that there are extra files.

I started doing this with my [phone](https://github.com/chapmanjacobd/phone) and it made formatting my phone painless. The hardest part is getting started. I still haven't added all my config files to git; I have a daily script that will remove one line from my [home directory](https://github.com/chapmanjacobd/computer/) gitignore so I can incrementally add config files. And it has already brought me a lot of peace of mind even if I'm only like 30% of the way done on the desktop.
