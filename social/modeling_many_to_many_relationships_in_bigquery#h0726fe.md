you can try with two tables if you treat BQ as a batch system and run it a few times a day

but if you want live results or if you need to update by id frequently you're going to eventually hit the concurrent update or DML updates per day limits
