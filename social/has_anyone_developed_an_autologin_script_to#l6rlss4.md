I don't think this is as useful on a headless device and it won't manage logins for you.

But if you want to test it out to see if it works be sure to use `--allow-immediate` with `tabsadd`. Without this it skips the first length of time. For example, with monthly frequency it won't open the tab until next month because it assumes that you visited the URL within the same month that you added it to the db.
