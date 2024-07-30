with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]

with ExitStack() as stack:
    files = []
    for idx in range(5):
        files.append(stack.enter_context(NamedTemporaryFile(suffix='.txt')))
