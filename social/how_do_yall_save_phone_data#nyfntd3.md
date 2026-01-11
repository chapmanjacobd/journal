I use Syncthing to sync everything between phone and computers (and backup to an offline disk) 

but for notes specifically I use git. It works really well for text. There are GUI apps out there for it. You can setup a git remote on any computer without a third server:

    git remote remove origin
    git config receive.denyCurrentBranch updateInstead

Then on your phone you just do something like this:

    git remote add server ssh://$user@computer/home/$user/notes/
    git branch --set-upstream-to=server/main main

The benefits of git is that sync conflicts are often easily merged. Tailscale helps with networking to connect these pieces together--though Syncthing works fine without Tailscale
