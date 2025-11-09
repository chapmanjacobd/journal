Hopefully you don't need this, but I made a little utility to help with converting the types of columns.

https://github.com/chapmanjacobd/computer/blob/main/bin/duckdb_typecaster.py

It finds the smallest data type that matches the data by looking at the first 1000 rows. It would be nice if there was a way to see all the values which don't match but I haven't found a performant way to do that. You can use `--force` to set those values to null though.
