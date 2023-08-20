I think you can just unnest twice. not sure if you can do that with function composition... I think you can do the following but you may need a subquery.

  


select id, expanded\_col from table, unnest(nestednested) unn1, unnest (unn1) expanded\_col
