hmm it doesn't work like that on my machine did you rebind some keys?

You can check with this:

    bind | grep --fixed-strings '\t'

Pressing the right arrow will expand out like you say but tab will only go to the next folder:

    bind --preset \t complete
    bind --preset \e\[C forward-char

You can use a temporary config to compare with what is default:

    sh -c 'env HOME=$(mktemp -d) fish'
