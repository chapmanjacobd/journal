This looks like a nice tool for Windows

On LInux you can use `dmesg --follow` or `lshw`

    sudo lshw -class disk -class tape -short
    H/W path               Device          Class          Description
    =================================================================
    /0/100/6/0/0           hwmon0          disk           NVMe disk
    /0/100/6/0/2           /dev/ng0n1      disk           NVMe disk
    /0/100/6/0/1           /dev/nvme0n1    disk           2TB NVMe disk
    /0/100/17/0            /dev/sda        disk           12TB ST12000NM001G-2M
    ...
