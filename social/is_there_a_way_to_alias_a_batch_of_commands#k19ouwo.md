I've been using this over the past few months to save abbreviations easily (as the built-in functionality was removed in Fish 3.6.0). A bit hacky but I've hit no bugs yet. note that this requires `sponge` from `moreutils`:

    function abbrsave
        abbr -a -- $argv[1] $argv[2..-1]

        filterfile $__fish_config_dir/abbreviations "abbr -a -- $argv[1] "
        echo abbr -a -- $argv[1] (string escape -- $argv[2..-1]) >> $__fish_config_dir/abbreviations
    end

    function filterfile --argument file
        for word in $argv[2..-1]
            if test -n "$word"
                grep -i "$word" "$file"
                grep -iv "$word" "$file" | sponge "$file"
            end
        end
    end

    funcsave abbrsave
    funcsave filterfile
    abbrsave abbr abbrsave

edit:

Then add this to config.fish:

    source $__fish_config_dir/abbreviations
