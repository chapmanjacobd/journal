If the explain output does not say something like USING TEMP BTREE INDEX ON (COL, ...) then the query likely didn't need an index. Sometimes the query planner is wrong but usually it is right
