I prefer this way: https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor

it's a bit easier to understand the flow:

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=2) as e:
        e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
        e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
        e.submit(shutil.copy, 'src3.txt', 'dest3.txt')

    print('all tasks done')

And, if it turns out your program is CPU-bound and not IO-bound, just replace Thread with Process above to use `ProcessPoolExecutor`.
