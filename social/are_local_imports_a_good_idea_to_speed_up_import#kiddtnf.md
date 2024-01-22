If you need to reference multiple modules after splitting them up you can also do something like this:

        def import_func():
            module = importlib.import_module(module_name)
            return getattr(module, function_name)()

as seen here: https://github.com/chapmanjacobd/library/blob/main/xklb/lb.py
