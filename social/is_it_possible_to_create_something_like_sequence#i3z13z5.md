if you want to use number ids you can use row\_number +(select max(id) subquery)

but if you do this you can NEVER do more than one load concurrently. It's better to use farmfingerprint in most cases
