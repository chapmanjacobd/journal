>  cp "${CONFDIR}/$1/kitty.conf" "${CONFDIR}/kitty.conf"

I don't think it is good practice to overwrite files to change configuration

>  kill -SIGUSR1 $(pidof kitty) 

If you are closing and re-opening kitty then I would just as soon, for example, alias `kcdark` in your shell to `kitty --config ~/.config/kitty/kitty_dark.conf`
