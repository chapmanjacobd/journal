import pandas as pd
from sqlalchemy import create_engine

def process_sql_using_pandas():
    engine = create_engine(
        "postgresql://postgres:pass@localhost/example"
    )
    conn = engine.connect().execution_options(
        stream_results=True)

    for chunk_dataframe in pd.read_sql(
            "SELECT * FROM users", conn, chunksize=1000):
        print(f"Got dataframe w/{len(chunk_dataframe)} rows")
        # ... do something with dataframe ...

if __name__ == '__main__':
    process_sql_using_pandas()

