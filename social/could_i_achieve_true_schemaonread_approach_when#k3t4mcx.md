It sounds like you have inconsistent schema across your data files. Optimally, you will solve this upstream. 

If you don't solve it then every analyst who works with the data in BigQuery will also need to either ignore the data which is not consistent or map the universe of the different schema types and caveats in their head. 

So it will be better if you can solve the problem before ingesting it. Schema validation can be a script that you write to ingest data and as you understand the oddities you can filter out the rows or files before they are uploaded to GCS.

I don't recommend the JSON data type in BigQuery because it is pretty slow to parse. If you can make everything normal table columns or STRUCT/ nested STRUCT then you will get much faster queries
