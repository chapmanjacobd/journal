If you have systemd and are a wheel user you can use `systemd-run` to fix session creation or PAM problems that stem from invalid configuration or excessive open file limits. 

This worked for me even when `pkexec su --session-command` and many other attempts did not
