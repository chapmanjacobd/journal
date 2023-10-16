That sounds expensive and difficult to program around but if you have fewer than 20,000 types of schemas you could make each schema its own table in BigQuery. But you can only reference 1000 tables in a single query.

I think you'll have a much easier time handling this in python
