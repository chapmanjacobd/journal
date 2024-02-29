> The script runs without delay if run from a terminal session, the delay only happens when running from launchd, or cron. 

Are you using the absolute path to ffmpeg? Is it cron running a script (ie. BASH?)?

> Sometimes it runs without delay. 

This makes me think it is likely not an ffmpeg issue but rather something in your environment. Maybe I/O bottleneck related
