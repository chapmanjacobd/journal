def traceclass(cls: type):
    def make_traced(cls: type, method_name: str, method: Callable):
        def traced_method(*args, **kwargs):
            print(f"--> Executing: {cls.__name__}::{method_name}()")
            return method(*args, **kwargs)

        return traced_method

    for name in cls.__dict__.keys():
        if callable(getattr(cls, name)) and name != "__class__":
            setattr(cls, name, make_traced(cls, name, getattr(cls, name)))
    return cls


def stacktrace(func=None, exclude_files=["anaconda"]):
    def tracer_func(frame, event, arg):
        co = frame.f_code
        func_name = co.co_name
        caller_filename = frame.f_back.f_code.co_filename
        if func_name == "write":
            return  # ignore write() calls from print statements
        for file in exclude_files:
            if file in caller_filename:
                return  # ignore in ipython notebooks
        args = str(tuple([frame.f_locals[arg] for arg in frame.f_code.co_varnames]))
        if args.endswith(",)"):
            args = args[:-2] + ")"
        if event == "call":
            print(f"--> Executing: {func_name}{args}")
            return tracer_func
        elif event == "return":
            print(f"--> Returning: {func_name}{args} -> {repr(arg)}")
        return

    def decorator(func: Callable):
        def inner(*args, **kwargs):
            settrace(tracer_func)
            func(*args, **kwargs)
            settrace(None)

        return inner

    if func is None:
        # decorator was used like @stacktrace(...)
        return decorator
    else:
        # decorator was used like @stacktrace, without parens
        return decorator(func)
