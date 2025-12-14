If you download one video at a time you could use the program `timeout`

example:

    timeout 2m wget2 --user-agent=$(
        python -c "from yt_dlp.utils.networking import random_user_agent; print(random_user_agent())"
    ) $url

For your question specifically though... have you tried using counting the time elapsed between progress_hooks? That should give you an answer. Keep a global variable with the time since last elapsed and then print the time between like this:

    class Timer:
        def __init__(self):
            self.reset()

        def reset(self):
            self.start_time = default_timer()

        def elapsed(self):
            if not hasattr(self, "start_time"):
                raise RuntimeError("Timer has not been started.")
            end_time = default_timer()
            elapsed_time = end_time - self.start_time
            self.reset()
            return f"{elapsed_time:.4f}"


    t = Timer()

    # later...
        global t
        log.debug("progress_hook time: %s", t.elapsed())
