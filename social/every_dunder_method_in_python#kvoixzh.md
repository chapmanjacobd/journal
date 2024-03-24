It's confusing to explain `__init__` without `__new__`

With `__init__` you might write `return None` but calling `T(a, b=3)` returns an object (self). The python documentation is better at explaining this:

> Because `__new__()` and `__init__()` work together in constructing objects no non-None value may be returned by `__init__()`

https://docs.python.org/3/reference/datamodel.html#object.__init__
