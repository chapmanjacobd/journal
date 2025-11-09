I don't think there's a good way to do this for any serious usage. If people are motivated enough there are still ways that they could infer if they had IO access of the file--or if the admin can frequently fetch the dbPollUser status to know when they submitted the answer.

But essentially you could use a random value instead of sequential for a primary key and create a WITHOUT ROWID table. 

https://www.sqlite.org/withoutrowid.html
