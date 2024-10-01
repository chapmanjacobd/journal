hmm I'm unable to reproduce this locally. If there are no unstaged/untracked files then pressing tab does nothing but I can also backspace. When there are unstaged or untracked files then pressing tab autocompletes the matching files.

    git status --untracked

I'm using fish 3.7.0

I would check `/usr/share/fish/completions/git.fish` (or the equivalent path for Mac OS)

You can launch a default fish session without needing to delete or reinstall anything like this:

    sh -c 'env HOME=$(mktemp -d) fish'
