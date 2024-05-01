hmm not sure about this specifically but if you ever need something even marginally more complicated than the above you'll probably want to switch to the python interface to have a more granular control about the logging:


    ydl_log = {"error": [], "warning": [], "info": []}

    class DictLogger:
        def debug(self, msg):
            if msg.startswith("[debug] "):
                pass
            else:
                self.info(msg)

        def info(self, msg):
            ydl_log["info"].append(msg)

        def warning(self, msg):
            ydl_log["warning"].append(msg)

        def error(self, msg):
            ydl_log["error"].append(msg)
        
    ydl_opts = {
        "logger": DictLogger(),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(webpath, download=True)

from https://github.com/chapmanjacobd/library/blob/9cca5d318db79e1acb7dbfb5e65c54cf84d707a4/xklb/createdb/tube_backend.py#L321
