> && nohup

should probably be `; nohup`. If the process is not running then `killall` will exit nonzero. But this should really just be a systemd service
