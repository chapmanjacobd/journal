Yeah, you could run it and always decline the confirmation prompt and copy and paste the ALTER statements that you want (for each specific column) into a duckdb prompt

If you want the original and new column I guess you could use something like a generated column with SAFE_CAST

https://duckdb.org/docs/sql/statements/create_table.html#generated-columns
