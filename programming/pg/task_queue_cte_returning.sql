with rows_to_be_deleted as materialized (
    select * from task_queue
    where queue_group_id = 15
    fetch first 1 rows only
    for update skip locked
)
delete from task_queue
where id in (select id from rows_to_be_deleted)
returning item_id;
