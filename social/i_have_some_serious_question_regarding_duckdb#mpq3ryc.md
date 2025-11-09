I spent a couple weeks giving it a good thorough try. In terms of performance... it's a mixed bag.

I would use it over SQLite with WORM or OLAP data for its more expressive SQL dialect and the duckdb REPL is just a bit nicer... The default of limiting output to a small number of rows also makes it feel fast. The `EXPLAIN ANALYZE` is extremely beautiful. The aesthetics and marketing are best-in-class. But SQLite in WAL mode can be much faster at updating or inserting records--especially for any real-world non-trivial tables. 

I don't think DuckDB can ever completely replace SQLite for all use cases but it can often be the best tool for the job--even when querying SQLite files. For example, the `format_bytes()` function is very convenient...

DuckDB has gotten a lot better in recent years there are still a few sharp edges. For example, one such query that blocked me from moving from SQLite to DuckDB looked like this:

    SELECT
        m.id AS id
        , SUM(CASE WHEN h.done = 1 THEN 1 ELSE 0 END) AS play_count
        , MIN(h.time_played) AS time_first_played
        , MAX(h.time_played) AS time_last_played
        , FIRST_VALUE(h.playhead) OVER (PARTITION BY h.media_id ORDER BY h.time_played DESC) AS playhead
        -- , *  -- SQLite even lets you do this... but I concede that is a bit extreme...
    FROM media m
    JOIN history h ON h.media_id = m.id
    GROUP BY m.id;

It would give me this error:

    Error: column "playhead" must appear in the GROUP BY clause or must be part of an aggregate function.
    Either add it to the GROUP BY list, or use "ANY_VALUE(playhead)" if the exact value of "playhead" is not important.
    LINE 6:     FIRST_VALUE(h.playhead) OVER (PARTITION BY h.media_id ORDER BY h.time_played DESC) AS playhead

If I changed the last line to

    GROUP BY m.id, h.media_id, h.time_played, h.playhead;

I wouldn't get an error but that query is not asking for the same thing as the original query which is selecting the most recent playhead value instead.

SQLite also supports non-UTF8 data which is [handy when dealing with arbitrary file paths](https://dwheeler.com/essays/filenames-in-shell.html) and other pre-sanitized data... even Full-Text Search works for the UTF-8 encode-able bytes. [DuckDB struggles with this](https://github.com/duckdb/duckdb/discussions/16049).
