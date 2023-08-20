Yesterday: Tried building an `ncdu` clone with `textual` but couldn't get it to work. Ended up making a non-TUI `ncdu` alternative instead:

    lb du -h
    usage: library disk-usage DATABASE [--sort-by size | count] [--depth DEPTH] [PATH / SUBSTRING SEARCH]

        Only include files smaller than 1kib

            library disk-usage du.db --size=-1Ki
            lb du du.db -S-1Ki
            | path                                  |      size |   count |
            |---------------------------------------|-----------|---------|
            | /home/xk/github/xk/lb/__pycache__/    | 620 Bytes |       1 |
            | /home/xk/github/xk/lb/.github/        |    1.7 kB |       4 |
            | /home/xk/github/xk/lb/__pypackages__/ |    1.4 MB |    3519 |
            | /home/xk/github/xk/lb/xklb/           |    4.4 kB |      12 |
            | /home/xk/github/xk/lb/tests/          |    3.2 kB |       9 |
            | /home/xk/github/xk/lb/.git/           |  782.4 kB |    2276 |
            | /home/xk/github/xk/lb/.pytest_cache/  |    1.5 kB |       5 |
            | /home/xk/github/xk/lb/.ruff_cache/    |   19.5 kB |     100 |
            | /home/xk/github/xk/lb/.gitattributes  | 119 Bytes |         |
            | /home/xk/github/xk/lb/.mypy_cache/    | 280 Bytes |       4 |
            | /home/xk/github/xk/lb/.pdm-python     |  15 Bytes |         |

        Only include files with a specific depth

            library disk-usage du.db --depth 19
            lb du du.db -d 19
            | path                                                                                                                                                                |     size |
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
            | /home/xk/github/xk/lb/__pypackages__/3.11/lib/jedi/third_party/typeshed/third_party/2and3/requests/packages/urllib3/packages/ssl_match_hostname/__init__.pyi        | 88 Bytes |
            | /home/xk/github/xk/lb/__pypackages__/3.11/lib/jedi/third_party/typeshed/third_party/2and3/requests/packages/urllib3/packages/ssl_match_hostname/_implementation.pyi | 81 Bytes |

    positional arguments:
    database
    working_directory

If you want to use this you need to first create a database:

    lb fsadd --filesystem du.db ./folders ./that ./you ./want ./to ./scan

If you have many clusters of machines you can create a database per machine then merge them together:

    lb mergedbs -h
    usage: library merge-dbs DEST_DB SOURCE_DB ...

But you will probably get better performance from querying multiple databases individually with something like GNU Parallel

Today: adding some sorely needed unit tests: https://github.com/chapmanjacobd/library/commit/bd2e138897fdf41b8d8eade89bcdb34fee2b6abd
