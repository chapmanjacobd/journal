It's because the query part needs to be a single string:

For example:


    $ sqlite3 :memory: select 1
    -- Loading resources from /home/xk/.sqliterc
    Error: in prepare, incomplete input

versus

    $ sqlite3 :memory: "select 1"
    -- Loading resources from /home/xk/.sqliterc
    QUERY PLAN
    `--SCAN CONSTANT ROW
    ┌───┐
    │ 1 │
    ├───┤
    │ 1 │
    └───┘

With the above command sqlite3 is only seeing ".import" as the query statement

Also, just some additional info: it is convention for POSIX commands to use optional args before positional args, but most tools, including sqlite3 are lenient: https://stackoverflow.com/a/61645523/697964
