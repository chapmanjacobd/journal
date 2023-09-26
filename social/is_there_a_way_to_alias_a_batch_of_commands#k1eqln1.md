Yes. post-3.6.0 `abbr` only exist per session unless you write them in config.fish. That's what these functions do. it creates an abbreviations file next to config.fish.

Ah yeah I forgot to mention that you need to add this to config.fish:

    source $__fish_config_dir/abbreviations
