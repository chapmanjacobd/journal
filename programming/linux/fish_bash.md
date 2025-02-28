# Run bash in fish

```fish
function \$
    if not test -f $XDG_RUNTIME_DIR/bash_daemon.pid; or not kill -0 (cat $XDG_RUNTIME_DIR/bash_daemon.pid) 2>/dev/null
        echo "Starting bash daemon..."
        bash ~/scripts/bash_daemon.sh &
        sleep 0.5
    end

    echo "$argv" > $XDG_RUNTIME_DIR/bash_daemon_pipe &

    while read -l line
        if test "$line" = "###DONE###"
            break
        end

        echo $line
    end < $XDG_RUNTIME_DIR/bash_daemon_out
end
```

## ~/scripts/bash_daemon.sh

```bash
#! /usr/bin/env bash

rm -f $XDG_RUNTIME_DIR/bash_daemon_pipe $XDG_RUNTIME_DIR/bash_daemon_out
mkfifo $XDG_RUNTIME_DIR/bash_daemon_pipe
mkfifo $XDG_RUNTIME_DIR/bash_daemon_out

echo $$ > $XDG_RUNTIME_DIR/bash_daemon.pid

while true; do
    read cmd < $XDG_RUNTIME_DIR/bash_daemon_pipe
    { eval "$cmd"; echo "###DONE###"; } > $XDG_RUNTIME_DIR/bash_daemon_out
done
```
