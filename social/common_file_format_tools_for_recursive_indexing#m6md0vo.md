Yeah, I think parquet is a great format for your use case. The only other thing you might try if it is only a compression problem is zstd. You can compress CSV like this:

    zstd -19 *.csv

Then pipe to xsv or grep/rg for various operations, etc:

    zstdcat latest.csv.zstd | xsv select path | rg -i exe

Parquet also supports zstd compression but brotli or snappy might compress better
