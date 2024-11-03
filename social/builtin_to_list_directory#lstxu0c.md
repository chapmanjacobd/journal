This works and is probably the most universal way:

    $ echo *
    fish: No matches for wildcard '*'. See `help wildcards-globbing`.
    echo *
         ^
    $ myglob=* echo $myglob
    
    # ^^ no error ^^

I would use fd or find in this case. But if using only built-ins I would use `for`. doesn't seem to error in this case: 

    for x in *
        if test -f $x
            echo $x
        end
    end

If you use this a lot you can make an abbreviation for it:

    abbr -a --set-cursor=! -- for for\ s\ in\ \*\n!\ \$s\nend

This works for `subdir/*` too

Also you can use `*/` to only match directories (eg. `subdir/*/`)

> For most commands, if any wildcard fails to expand, the command is not executed, [$status](https://fishshell.com/docs/current/language.html#variables-status) is [set](https://fishshell.com/docs/current/cmds/set.html) to nonzero, and a warning is printed. This behavior is like what bash does with `shopt -s failglob`. There are exceptions, namely [set](https://fishshell.com/docs/current/cmds/set.html) and [path](https://fishshell.com/docs/current/cmds/path.html), overriding variables in [overrides](https://fishshell.com/docs/current/language.html#variables-override), [count](https://fishshell.com/docs/current/cmds/count.html) and [for](https://fishshell.com/docs/current/cmds/for.html). Their globs will instead expand to zero arguments (so the command won't see them at all), like with `shopt -s nullglob` in bash.


> https://fishshell.com/docs/current/language.html#wildcards-globbing
