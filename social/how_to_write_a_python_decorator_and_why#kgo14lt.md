yup that's why you can call decorators like functions to create new functions similar to `functools.partial`

for example:


    def with_timeout(seconds):
        def decorator(decorated):
            @functools.wraps(decorated)
            def inner(*args, **kwargs):
                pool = multiprocessing.Pool(1)
                async_result = pool.apply_async(decorated, args, kwargs)
                try:
                    return async_result.get(seconds)
                finally:
                    pool.close()

            return inner

        return decorator

    munge_book_tags_fast = processes.with_timeout(70)(munge_book_tags)
    munge_book_tags_slow = processes.with_timeout(350)(munge_book_tags)

    munge_book_tags_fast(blah)
