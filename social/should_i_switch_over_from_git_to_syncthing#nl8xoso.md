Syncthing doesn't really do line-level conflict resolution. You can reduce conflicts in git by pulling often and you can choose to have git [likely often destructively] "resolve" conflicts by itself*--but you'll need to communicate this so that people _want_ to make sure they are up-to-date before making changes to the system and then they can have a way to verify that their changes made it in. Honestly, I don't see much benefit to using libgit2. Just keep things simple and focus on the UI, how users will interact with it

\* from the git side of things you could spit out the conflict information to logs and display it to the user but then do 

    git merge --abort; git rebase --abort; git add .; git reset HEAD --hard; git pull

to destroy the conflicts and get back up to date (maybe you'd need to fine-tune this but that should take care of it 99% of the time)

edit: you might also want to look into something like dolt https://www.dolthub.com/blog/2022-08-17-dolt-turbine/

---

Also, it is possible to use both Git and Syncthing at the same time: just put "/.git/" in `.stignore` if the git root is the same or lower folder depth than the Syncthing `.stfolder` marker. **So it's not necessarily an either/or thing**. I use git to sync most of my computers home folder but I use Syncthing in addition to that for my laptop and desktop .config and .local folders

- https://github.com/chapmanjacobd/computer/blob/main/.config/.stignored
- https://github.com/chapmanjacobd/computer/blob/main/.local/.stignored

If you just need to move data--it's possible to move git patches through ssh--so maybe you don't really need Syncthing. I do this all the time:

https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/gitcopy.fish
