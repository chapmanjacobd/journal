WITH duplicates AS (
    SELECT id, ROW_NUMBER() OVER(
        PARTITION BY firstname, lastname, email
        ORDER BY age DESC
    ) AS rownum
    FROM contacts
)
DELETE FROM contacts
USING duplicates
WHERE contacts‍.‍id = duplicates‍.‍id AND duplicates‍.‍rownum > 1;
