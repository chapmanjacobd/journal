tl;dr: choose the best tool for the job

Databases have limitations for performing complex analytical algorithms compared to languages like R and Python. There are many high-quality libraries available in R and Python that enable advanced analysis (e.g. https://gitlab.com/shekhand/mcda).

Databases excel at interactive queries and extracting _subsets_ of data. Combining SQL with Python or R can be very powerful for repeating analyses on different parameters.

However, if your analysis requires reading the **full** dataset into Python each time, there is little benefit to using a database. In this case, a format like Parquet will load faster than querying a database and extracting all rows/columns.
