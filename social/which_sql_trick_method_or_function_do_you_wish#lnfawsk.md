`MINUS` Operator: subtract table1 from table2. It is basically the opposite of `UNION`

For SQL engines that don't have `UNNEST`:

    SELECT CASE WHEN column1 = 1 THEN table1.val1 
                WHEN column1 = 2 THEN table1.val2
                ...
           END as val
    FROM table1
    CROSS JOIN (1,2,3, ...)
