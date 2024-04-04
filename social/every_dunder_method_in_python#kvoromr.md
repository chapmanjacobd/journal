Still, I think the article could be improved to be more clear. You have `T(a, b=3)` map to `T.__init__(x, a, b=3)` and returning `None`. I think it's fine to not mention `T.__new__` at that point but changing Operation `T(a, b=3)` in the first table to `Initialization of T(a, b=3)` would be more clear--or instead of `None` say `return value not accessible` or `N/A` because it is a side effect function conceptually inside of `__new__()`