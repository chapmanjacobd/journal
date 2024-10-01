I think time spent deliberating over whether a file belongs in X or Y folder is better spent naming files appropriately, developing a constrained vocabulary, and learning system tools for searching like voidtools Everything or find, fd-find, grep, rg, [rga](https://github.com/phiresky/ripgrep-all), etc.

For example, it is easy to search for recently modified files within a certain time range:

    fd -tf --changed-within '3 days' --changed-before '1 day'

The fewer folders you have, the easier it is to choose where to save things
