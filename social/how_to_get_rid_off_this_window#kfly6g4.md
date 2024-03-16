instead of running `brave` you could run it with setsid like this: `setsid -f brave`.

You can abbreviate this to `run`, example using fish shell:

    function run --wraps=setsid
        setsid -f $argv
    end

then you can do `run brave`.

If you use BASH you could create a double subshell and background the command within it: `($(brave) &)`

or nohup: `nohup brave &`
