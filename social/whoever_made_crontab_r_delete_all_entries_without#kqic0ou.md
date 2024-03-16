yeah here are some useful shell abbreviations:

- timers: systemctl --user list-timers --all --no-pager --no-legend
- timer-status: journalctl --no-hostname --reverse -a --user -u $timers_service

create from CLI:

    function systemd-cron
        # systemd-cron unit_name calendar_str cmd to run
        set unit $argv[1]
        set cal $argv[2]
        set cmd $argv[3..-1]
    
        echo "[Service]
    Type=simple
    RemainAfterExit=no
    TimeoutStartSec=infinity
    ExecStart='/usr/bin/fish' '-c' '$cmd'
    " >~/.config/systemd/user/$unit.service
    
        echo "[Timer]
    Persistent=yes
    OnCalendar=$cal
    
    [Install]
    WantedBy=timers.target
    " >~/.config/systemd/user/$unit.timer
    
        touch ~/.local/share/systemd/timers/stamp-$unit.timer
        systemctl --user daemon-reload
        systemctl --user enable --now $unit.timer
        systemctl --user list-timers --no-pager --all
    end

or delete

    function systemd-cron-delete --argument unit
        systemctl --user disable --now $unit.timer
        rm ~/.config/systemd/user/$unit.service
        rm ~/.config/systemd/user/$unit.timer
        systemctl --user list-timers --no-pager --all
    end


check your systemd calendar string:

    $ systemd-analyze calendar 'Mon *-11-14..21 13:15'
      Original form: Mon *-11-14..21 13:15
    Normalized form: Mon *-11-14..21 13:15:00
    Next elapse: Mon 2024-11-18 13:15:00 HKT
       (in UTC): Mon 2024-11-18 05:15:00 UTC
       From now: 9 months 2 days left
