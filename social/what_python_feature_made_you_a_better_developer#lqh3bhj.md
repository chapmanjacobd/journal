I think both articles are good and they don't contradict each other.

Ultimately, the "problem" is that `sync` handles `async` for us by handling all the async side effects (like HTTP calls, `io_uring`, etc) by blocking conservatively but most programs can be doing other things while waiting
