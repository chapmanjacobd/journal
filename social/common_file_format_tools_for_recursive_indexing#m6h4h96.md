`plocate` is very performant and it uses a custom database.

SQLite can support [various types of indexes](https://www.sqlite.org/expridx.html), and can likely be read by future computers for a very long time.

I think the main reason why there is no dominant inter-operable format is because different tools benefit from storing data in a different way--ie. different types of indexes.

I wrote [a bunch of different tools](https://github.com/chapmanjacobd/library) that work with SQLite files but it's not as fast as `plocate`--even with SQLite trigram indexes

> nor really any CLI tools that seem to be centered around saving the results to some kind of standard/consistent file format

nushell is pretty good at this! It does have its quirks... but it's my preferred shell when using Windows. (but fish shell might be ported to Windows soon--the benefits of being able to pipe binary (structured) data has additional operational complexity which often does not justify itself over simple "stringly"-typed programs)

well... actually the operating word of your sentence is _saving_ and nushell [actually doesn't do that too well](https://github.com/nushell/nushell/issues/2731) either... or at least it's not part of regular, idiomatic use

But since you brought it up parquet is a great format! I'd recommend that almost as much as SQLite, though there are currently far fewer programs that work with Parquet I expect that to grow (at least in the short term--it's hard to predict the [Lindy](https://en.wikipedia.org/wiki/Lindy_effect)-ness of any specific thing)
