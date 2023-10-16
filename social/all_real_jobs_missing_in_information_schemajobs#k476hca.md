I've noticed something like this too. I wonder if it only shows Interactive jobs or Batch jobs but the documentation says that it should show ALL jobs within the last 180 days.

https://cloud.google.com/bigquery/docs/information-schema-jobs-by-organization

Maybe double check your account permissions:

JOBS_BY_ORGANIZATION requires `bigquery.jobs.listAll` just because you have Org Admin does not mean you have that specific permission

maybe a ticket should be opened: https://issuetracker.google.com/issues?q=JOBS_BY_PROJECT
