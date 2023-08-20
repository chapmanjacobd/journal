if you're trying to sync up multiple computers what I do is use syncthing. you won't have as much control but if your computers are online at the same time frequently enough to overlap a couple times a week it's a good solution and you shouldn't have many sync conflicts. 

I sync ~/.config and ~/.local. just make sure to .stignore the folders which syncthing uses for it's local database lol. I've posted before about some other folders you might want to ignore.

For fish shell specifically the only problem I encountered is if you use the computers at the same time then you'll need to do something like this:
 
     cat ~/.local/share/fish/fish_history.sync-conflict-* >> ~/.local/share/fish/fish_history
     rm ~/.local/share/fish/fish_history.sync-conflict-*

If you haven't used syncthing before though I'd recommend using it on a simple folder until you get a sense for how it works. If you already have existing config folders on each machine syncthing will combine all of your ~/.config folders when you add the machine so if you're running KDE4 and another computer is running KDE5 or something like that then you could end up with invalid config. 

Backup before you start in case something goes awry. I've only done this after copying my personalized ~/.config to each machine first and I only use Fedora/openSUSE so things aren't super different. If you were mixing another distribution or OS like Arch or OpenBSD or Mac OS then config or data files are more likely to be incompatible
