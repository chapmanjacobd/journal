This isn't really fish shell specific, but you're on the right track. Use setsid -f

    function run --wraps=setsid
        setsid -f $argv
    end

edit: If the problem is that the application finishes immediately, like xdg-open, there isn't really a good option other than to use something like `gum confirm` after running the program to continue with the script
