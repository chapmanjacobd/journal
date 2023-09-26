I assume you don't get the error if you do:

    sh -c 'env HOME=$(mktemp -d) fish'

I would use grep or rg to find the file:

    rg -i --no-heading --no-line-number -j1 -. '/ 10'

search in `~/.config/fish/` and possibly `~/.bash*`, `/etc/profile`, or `/etc/profile.d/` if you use `bass`
