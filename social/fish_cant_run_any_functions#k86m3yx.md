Maybe you need to do this?

    fish_add_path ~/homebrew/bin/

I wonder if some files in the install script tried to copy to a hardcoded path.

    /usr/share/fish/functions/fish_config.fish

That's the location where fish_config lives on my machine. Maybe try reinstalling with brew. if that doesn't work try installing from the sources:

    wget https://github.com/fish-shell/fish-shell/releases/download/3.6.1/fish-3.6.1.tar.xz
    cmake .; make
    make install -h

Or try the .app which doesn't need installation:

    https://github.com/fish-shell/fish-shell/releases/download/3.6.1/fish-3.6.1.app.zip
