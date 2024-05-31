Yes, this is normal. This isn't an error from xdg-open but rather it is a warning from your PDF reader.

You can "hide" these types of warnings by opening similar to how launching on the desktop works:

Use `setsid -f firefox` instead of running `firefox &`, for example.

But I realize this advice only works for launching GUI programs directly and it does not work for `xdg-open`.

I think the easiest way would be to wrap xdg-open in a shell function to something like `xdg-open $@ >/dev/null 2>&1`

To actually fix the specific error you've shown you'll edit the code for whatever PDF reader you use and recompile it.
