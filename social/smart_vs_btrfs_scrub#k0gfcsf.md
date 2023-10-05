Here's something else that I noticed recently:

    # smartctl -A /dev/sdj
    /dev/sdj        197 Current_Pending_Sector  0x0032   200   200   000    Old_age   Always       -       3
    /dev/sdj        198 Offline_Uncorrectable   0x0030   100   253   000    Old_age   Offline      -       0

    # btrfs scrub status /mnt/d3
    UUID:             6ac6c182-84bf-4fc6-a1fd-ba37b8b578a9
    Scrub started:    Sun Sep 10 23:02:47 2023
    Status:           finished
    Duration:         7:43:41
    Total to scrub:   2.22TiB
    Rate:             83.24MiB/s
    Error summary:    read=96
      Corrected:      40
      Uncorrectable:  56
      Unverified:     0

    # btrfs device stats -T /mnt/d3
    Id Path      Write errors Read errors Flush errors Corruption errors Generation errors
    -- --------- ------------ ----------- ------------ ----------------- -----------------
     1 /dev/sdj1            0           0            0                 0                 0


Pending uncorrectable sectors will show up in scrub but not in device stats

edit:

you can also check the smartd service:

    $ journalctl --no-hostname --reverse -u smartd
    ...
    Sep 14 20:55:06 smartd[1282]: Device: /dev/sdj [SAT], 1 Currently unreadable (pending) sectors (changed -2)
    Sep 14 20:25:06 smartd[1282]: Device: /dev/sdj [SAT], 3 Currently unreadable (pending) sectors
    ...
    Sep 11 06:55:06 smartd[1282]: Device: /dev/sdj [SAT], 3 Currently unreadable (pending) sectors (changed +2)
    Sep 11 06:25:07 smartd[1282]: Device: /dev/sdj [SAT], 1 Currently unreadable (pending) sectors
