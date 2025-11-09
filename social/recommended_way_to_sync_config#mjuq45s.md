I put my whole homefolder in git to keep 7 PCs in sync, and additionally, use syncthing between my main PC and my main laptop to sync `.config` and `.local`:

- https://github.com/chapmanjacobd/computer/blob/main/.local/.stignored
- https://github.com/chapmanjacobd/computer/blob/main/.config/.stignored

I also have encountered issues with fisher but after doing this (one time after OS install) things work fine:

    curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher (cat ~/.config/fish/fish_plugins)

I don't sync between macOS and Linux though so unfortunately I don't have experience to share about that
