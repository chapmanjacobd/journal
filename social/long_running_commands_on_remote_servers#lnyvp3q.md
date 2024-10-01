You can also use nohup

Or setsid -f

Or systemd-run

Or run the command in a double nested subshell

Or &; disown %1

But if you want to check on the command later using tmux is the easiest. 

    ssh remotepc -t tmux new-session -A -s phone

systemd has its own learning curve and the other options you would have to use ps or pgrep/pkill to manage the process; and cat the output from /proc (or the nohup output file; or pipe to systemd-cat and check the journal)
