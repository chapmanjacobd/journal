SELECT dates_without_gaps‍.‍day, COALESCE(SUM(statistics‍.‍count), 0)
FROM generate_series(
    CURRENT_DATE - INTERVAL '14 days',
    CURRENT_DATE,
    '1 day'
) as dates_without_gaps(day)
LEFT JOIN statistics ON(statistics‍.‍day = dates_without_gaps‍.‍day)
GROUP BY dates_without_gaps‍.‍day;
