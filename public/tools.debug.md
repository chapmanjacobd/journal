strace -p (pgrep lb)
perf
sudo iftop -n -b -P -t -o 40s -L 4
iostat
nmon
lsof
pidstat -r -p (pgrep mpv) 2 10
mpstat 2 5
