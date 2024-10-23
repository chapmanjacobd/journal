ah yeah it looks like fish has an example function in [the release notes](https://github.com/fish-shell/fish-shell/releases/tag/3.6.0) of 3.6.0:

    function multicd
        echo (string repeat -n (math (string length -- $argv[1]) - 1) ../)
    end
    abbr --add dotdot --regex '^\.\.+$' --function multicd
