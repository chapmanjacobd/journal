You could use something like dbt (or script a more minimal tool) to re-create views and procedures. Test all changes on a temp db then deploy to production.

But this is easiest/cleanest for databases which support transactional DDL.
