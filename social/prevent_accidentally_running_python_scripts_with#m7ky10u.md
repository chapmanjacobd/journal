I do this:

    mkexecpy ~/bin/*.py

where mkexepy is this fish function:

    function mkexecpy
        for f in $argv
            if not grep -q '^#!' $f
                echo "#!/usr/bin/python3" | cat - $f | sponge $f
            end
    
            chmod +x $f
        end
    end

This requires `moreutils`... if anyone knows of an easier way of prepending a line, let me know!
