alright ! I did some tests and I'm pretty happy with the results 

    truncate -s1G d1.img
    truncate -s1G d2.img
    truncate -s1G d3.img
    truncate -s1G d4.img
    ld1=$(sudo losetup --show --find d1.img)
    ld2=$(sudo losetup --show --find d2.img)
    ld3=$(sudo losetup --show --find d3.img)
    ld4=$(sudo losetup --show --find d4.img)

    sudo mkfs.btrfs -d raid1 -m raid1c4 "$ld1" "$ld2" "$ld3" "$ld4" 
    sudo mkdir -p /mnt/test
    sudo mount "$ld1" /mnt/test

    sudo dd if=/dev/zero of=/mnt/test/file bs=1M count=500

    sudo btrfs fi balance start /mnt/test/

    ~ 🃆 sudo btrfs device usage /mnt/test
    /dev/loop0, ID: 1
        Device size:             1.00GiB
        Device slack:              0.00B
        Data,RAID1:            416.00MiB
        Metadata,RAID1C4:      138.25MiB
        System,RAID1C4:         32.00MiB
        Unallocated:           437.75MiB

    /dev/loop1, ID: 2
        Device size:             1.00GiB
        Device slack:              0.00B
        Data,RAID1:            416.00MiB
        Metadata,RAID1C4:      138.25MiB
        System,RAID1C4:         32.00MiB
        Unallocated:           437.75MiB

    /dev/loop2, ID: 3
        Device size:             1.00GiB
        Device slack:              0.00B
        Data,RAID1:            416.00MiB
        Metadata,RAID1C4:      138.25MiB
        System,RAID1C4:         32.00MiB
        Unallocated:           437.75MiB

    /dev/loop3, ID: 4
        Device size:             1.00GiB
        Device slack:              0.00B
        Data,RAID1:            416.00MiB
        Metadata,RAID1C4:      138.25MiB
        System,RAID1C4:         32.00MiB
        Unallocated:           437.75MiB

    sudo dd if=/dev/random of=/dev/loop3

    ~ 🃏 sudo btrfs scrub start /mnt/test/
    scrub started on /mnt/test/, fsid c3af8361-eaa8-41ae-81f8-8b0911fa794e (pid=30375)
    ~ ⪖ WARNING: errors detected during scrubbing, corrected
    sudo
    ~ 🌌 sudo btrfs scrub status /mnt/test/
    UUID:             c3af8361-eaa8-41ae-81f8-8b0911fa794e
    Scrub started:    Mon Apr 11 22:41:13 2022
    Status:           finished
    Duration:         0:00:01
    Total to scrub:   1002.62MiB
    Rate:             1002.62MiB/s
    Error summary:    super=2 csum=98858
    Corrected:      98858
    Uncorrectable:  0
    Unverified:     0


    sudo dd if=/dev/random of=/dev/loop3
    sudo dd if=/dev/random of=/dev/loop1


    ~ 🦄 sudo btrfs scrub start /mnt/test/
    scrub started on /mnt/test/, fsid c3af8361-eaa8-41ae-81f8-8b0911fa794e (pid=30588)
    WARNING: errors detected during scrubbing, corrected
    ~ 🌛 sudo btrfs scrub status /mnt/test/
    UUID:             c3af8361-eaa8-41ae-81f8-8b0911fa794e
    Scrub started:    Mon Apr 11 22:42:37 2022
    Status:           finished
    Duration:         0:00:02
    Total to scrub:   1002.62MiB
    Rate:             501.31MiB/s
    Error summary:    super=4 csum=128061
    Corrected:      128061
    Uncorrectable:  0
    Unverified:     0

    sudo dd if=/dev/random of=/dev/loop3
    sudo dd if=/dev/random of=/dev/loop2

    ~ [1] 👮 sudo btrfs scrub start /mnt/test/
    scrub started on /mnt/test/, fsid c3af8361-eaa8-41ae-81f8-8b0911fa794e (pid=31480)
    ~ 🌞 ERROR: there are uncorrectable errors

    ~ 🌠 sudo btrfs scrub status /mnt/test/
    UUID:             c3af8361-eaa8-41ae-81f8-8b0911fa794e
    Scrub started:    Mon Apr 11 22:45:06 2022
    Status:           finished
    Duration:         0:00:01
    Total to scrub:   1002.62MiB
    Rate:             1002.62MiB/s
    Error summary:    super=4 csum=197698
    Corrected:      66
    Uncorrectable:  197632
    Unverified:     0

    ~ 🌛 ls -lah /mnt/test/
    Permissions Size User Date Modified Name
    .rw-r--r--  524M root 11 Apr 22:38  file

The file is still there ! lol (but I get IO error when trying to read it)

    ~ 🃆 sudo btrfs balance start -dconvert=raid10 -mconvert=raid1c3 /mnt/test
    ERROR: error during balancing '/mnt/test': Input/output error

of course... only recovers 2 disks with a certain disk orientation but that is still a great thing to have!

so I'm going to redo the first steps to setup our next test:

    sudo umount /mnt/test
    sudo losetup -d "$ld1" "$ld2" "$ld3" "$ld4"
    rm d1.img d2.img d3.img d4.img

    truncate -s1G d1.img
    truncate -s1G d2.img
    truncate -s1G d3.img
    truncate -s1G d4.img
    ld1=$(sudo losetup --show --find d1.img)
    ld2=$(sudo losetup --show --find d2.img)
    ld3=$(sudo losetup --show --find d3.img)
    ld4=$(sudo losetup --show --find d4.img)
    sudo mkfs.btrfs -d raid10 -m raid1c3 "$ld1" "$ld2" "$ld3" "$ld4"
    sudo mkdir -p /mnt/test
    sudo mount "$ld1" /mnt/test
    sudo dd if=/dev/zero of=/mnt/test/file bs=1M count=500

    sudo btrfs fi balance start /mnt/test/

allright now doing the same tests but for RAID10:


    @xk@bok:~> sudo dd if=/dev/random of=/dev/loop3
    dd: writing to '/dev/loop3': No space left on device
    2097153+0 records in
    2097152+0 records out
    1073741824 bytes (1.1 GB, 1.0 GiB) copied, 7.03123 s, 153 MB/s
    @xk@bok:~> sudo btrfs scrub start /mnt/test/
    scrub started on /mnt/test/, fsid 762315f2-54b4-4a69-9f76-4c1d6167c75a (pid=32743)
    @xk@bok:~> WARNING: errors detected during scrubbing, corrected

    @xk@bok:~> sudo btrfs scrub status /mnt/test/
    UUID:             762315f2-54b4-4a69-9f76-4c1d6167c75a
    Scrub started:    Mon Apr 11 22:52:24 2022
    Status:           finished
    Duration:         0:00:01
    Total to scrub:   1001.97MiB
    Rate:             1001.97MiB/s
    Error summary:    super=2 csum=64033
    Corrected:      64033
    Uncorrectable:  0
    Unverified:     0

one drive fail looks fine in RAID10. let's try two:

    sudo dd if=/dev/random of=/dev/loop3
    sudo dd if=/dev/random of=/dev/loop1

    @xk@bok:~> sudo btrfs scrub start /mnt/test/
    scrub started on /mnt/test/, fsid 762315f2-54b4-4a69-9f76-4c1d6167c75a (pid=364)
    @xk@bok:~> ERROR: there are uncorrectable errors

    @xk@bok:~> sudo btrfs scrub status /mnt/test/
    UUID:             762315f2-54b4-4a69-9f76-4c1d6167c75a
    Scrub started:    Mon Apr 11 22:54:17 2022
    Status:           finished
    Duration:         0:00:00
    Total to scrub:   1001.97MiB
    Rate:             0.00B/s
    Error summary:    super=4 csum=122478
    Corrected:      5602
    Uncorrectable:  116876
    Unverified:     0

nope :/ well ok 

ohhh huh... I did it a second time and used /dev/loop3 and loop2 instaed of loop3 and loop1 and it is able to recover it. That makes me feel a lot better. looks like RAID10 just chooses disk mirrors in a different order than RAID1 (?)

    Filesystem size:    4.00GiB
    Block group profiles:
    Data:             RAID10          204.75MiB
    Metadata:         RAID1C3         256.00MiB
    System:           RAID1C3           8.00MiB

    @xk@bok:~> sudo btrfs scrub status /mnt/test/
    UUID:             e946871b-9b4e-483e-9224-0dd913b855f8
    Scrub started:    Mon Apr 11 22:57:59 2022
    Status:           finished
    Duration:         0:00:01
    Total to scrub:   1001.92MiB
    Rate:             1001.92MiB/s
    Error summary:    super=2 csum=128076
    Corrected:      128076
    Uncorrectable:  0
    Unverified:     0


but this is a simple example... I should probably do the same thing with more than one block per disk. I wonder if the results would be different in that case?

final cleanup:

    sudo umount /mnt/test
    sudo losetup -d "$ld1" "$ld2" "$ld3" "$ld4"
    rm d1.img d2.img d3.img d4.img

(this exercise was done on 5.17.1-1-default)

TL;DR: BTRFS RULES!!
