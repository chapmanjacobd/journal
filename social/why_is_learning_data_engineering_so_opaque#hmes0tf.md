I would recommend learning BASH and Unix history/design principles next. You don't have to spend more than a few days on it--just enough to get a general feel.

With Microsoft/Azure being somewhat of an exception, everything else pretty much runs on BSD or Linux--and BASH is the glue which is somewhat universal: you can do a lot with pipes in BASH. 

Shell pipes are the original data pipelines. They have been around the longest. They aren't good for everything but GNU Parallel and a shell script can often be several orders of magnitude higher throughput than Hadoop. Not for every type of data or every operation mind you--but, if your data is line delimited, more often than not it can be a good option.

https://missing.csail.mit.edu/2020/data-wrangling/
