I'm interested in writing software to support something like this. But right now I'm not sure what the right interface would look like... also each person probably has an ideal workflow for how this might work so I'm unsure what a consensus would be

Here are a few random thoughts:

Syncthing is very good at moving or deleting files. If you trusted collaborators then you could likely use that. I use it myself for sorting or deleting files once across computers and phone.

You can use sqlite files in git by adding this to your .gitattributes file:

    *.db diff=sqlite3

but you could just as well use something like CSV with less noise.

I keep track of watch history by using rsync and custom scripts:

- https://github.com/chapmanjacobd/phone/blob/main/.config/fish/functions/lb-sync-phone.fish
- https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/copy_play_counts.py

I agree IPFS makes sense from a "global" URL perspective but I haven't really used it much

edit: Syncthing solves the problem of media sharing really efficiently (it dedupes sections of files so they don't need to go over the network if they've already been transferred) but it doesn't have an approve/reject workflow or selective sync built-in. 

I think syncthing would be a good platform to build on top of. You could create your own file-based workflow with some [slightly clever folder discipline](https://github.com/chapmanjacobd/computer/blob/main/bin/mktree.py) and then only syncing specific folders. For example, you have a `all/` folder for all media--maybe you sync that but you have it read only in syncthing, and then have writable folders that get synced back to the central server and you can see how people sort the files and delete them if they aren't in the correct location or something. This would create duplicate files until you dedupe against the `all/` folder. If you trust your collaborators more you could have `all/` be a writable folder and then you don't need to dedupe...

- https://github.com/syncthing/syncthing/issues/2491
- https://forum.syncthing.net/t/syncronization-by-approve/6184/4

Alternatively, it might make sense to write some custom code on top of syncthing. These might be interesting repos to look at:

- https://github.com/syncthing/syncthing-lite
- https://github.com/galilley/syncthing-pyselective

Might be interesting to compare some of these with Git Annex:

- https://github.com/no-src/gofs
- https://github.com/robehickman/BVersion
- https://github.com/elonen/lanscatter

Also:

- Resilio Sync: https://news.ycombinator.com/item?id=28863357
- HTTP open directories work pretty well for file sharing and distribution. `mpv` works well with servers that support HTTP Range requests. It might make sense to build something that takes inspiration from that--or build something on top of existing high-performance web platforms
- Distribution is at odds with curation. That is, distribution is movement and curation stops movement, at least until selection or approval. Traditionally curation happens before distribution--but it has two ends. For example, choosing which files are public on your website; or going to a website and finding something with Ctrl-F and then clicking download. Or a [grocery buyer](https://curtisfood.com/buyer-grocery/) who picks the products to stock the shelves at a store; or a customer who picks an item from the shelf. But there are probably other configurations that are possible
