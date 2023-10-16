I'm pretty sure `bq` works in Termux:

    termux-setup-storage
    pip install --upgrade requests pip wheel
    pip install google-cloud-sdk

You could write out queries in whatever editor you want, even Android apps. Then:

    bq query --use_legacy_sql=false --format=csv \
      --max_rows 2147483647 $(cat my_query.sql)

Or if you copy a query to your clipboard:

    bq query $(termux-clipboard-get)
