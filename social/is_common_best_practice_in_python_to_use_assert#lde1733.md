I would definitely prefer an error at the start of the script if you aren't setting default values. `None` is not always automatically better than an exception

> The more standard way

Just because it is the way that you do it does not mean it is more common. Searching GitHub using environ as a dict is almost twice as common:

- https://github.com/search?q=os.environ.get&type=code
- https://github.com/search?q=os.environ%5B&type=code

But I agree that os.environ.get is better than using os.getenv because os.putenv is broken
