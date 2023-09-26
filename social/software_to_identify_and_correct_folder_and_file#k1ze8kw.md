If you are on Linux of course I have to mention `detox` (https://github.com/dharple/detox) but I've honestly been bitten by that tool in more ways than one so I created my own tool. 

However, my own tool has become somewhat aggressive too; especially in this way: I wanted to remove sync errors on exFAT which only supports one folder of a given case so for example a folder named "SECURE" will create a sync conflict with a folder named "Secure". So I make all folders that have no dash, underscore, space, or dot in the middle of the folder name to be completely lowercase and for folder names with those things they become title case. This choice is arbitrary but I'm thinking about making it non-default so I don't need to caveat it every time I tell people about my tool.

Definitely do not run detox or my tool on system or program directories. It will mess everything up.

You will also need to create a fs database first via `library fsadd --filesystem dbname.db list of paths you want to scan`.

    $ library christen --help
    usage: library christen DATABASE [--run]
    
        Rename files to be somewhat normalized
    
        Default mode is dry-run
    
            library christen fs.db
    
        To actually do stuff use the run flag
    
            library christen audio.db --run
    
        You can optionally replace all the spaces in your filenames with dots
    
            library christen --dot-space video.db
    
    positional arguments:
      paths
    
    options:
      -h, --help       show this help message and exit
      --dot-space
      --overwrite, -f
      --run, -r
      --verbose, -v

https://github.com/chapmanjacobd/library
