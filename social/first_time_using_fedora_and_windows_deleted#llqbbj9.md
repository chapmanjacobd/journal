I used to dual boot Windows but after I didn't boot into Windows for over a year I decided to use that SSD for other purposes.

Recently I had the need to run a few `exe` that didn't work with wine and I discovered quickemu! If you can use a VM it is much faster than installing Windows normally:

    git clone --filter=blob:none https://github.com/wimpysworld/quickemu
    quickget windows 11
    ./quickemu --vm windows-11.conf --display spice

But this won't work for something like installing BIOS updates
