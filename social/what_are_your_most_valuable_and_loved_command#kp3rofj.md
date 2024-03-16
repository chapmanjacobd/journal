There's a lot out there:

- ssh, nomachine
  - ssh pakon -f -L 4102:localhost:4000 'sleep 10'; /usr/NX/bin/nxplayer --session ~/.ssh/pakon.nxs
- `code` to open a file or folder in VS Code
- fd-find, rg
- GNU Parallel
- strace
- search history shortcut for your terminal (for example `ctrl-shift-h` in kitty)
- zoxide to autojump to different folders
- `iostat -xh 4`
- `sudo iftop -n -b -P -t -o 40s -L 4`
- `ps -o pid,etime,%cpu,command ww`
- zombies: `ps axo pid=,stat= | awk '$2~/^Z/ { print $1 }'`
- pgrep, pkill
- gitls, gitls -1: 

        git ls-files --sparse --full-name -z | 
          xargs -0 -I FILE -P 20 git log $argv --date=iso-strict-local \
          --format='%ad %>(14) %cr %<(5) %an  %h ./FILE' -- FILE | 
          sort --general-numeric-sort

- openfiles: `sudo fatrace -f C | grep -vE '[CWO] /$|(deleted)'`
- filehandlers: `lsof -n -t $file`
- filehandles: 

        sudo lsof +c0 (mount | awk '{print $3}') 2>/dev/null | 
          grep -vE '^COMMAND' | awk '{print $1}' | sort | uniq -c | sort -g

- I wrote a [bunch of utilities](https://github.com/chapmanjacobd/library). Recently I've been heavily using 
    - `cluster-sort` to sort similar lines of text together by grouping TF-IDF with kmeans
    -  `links-add` to scrape links from paginated websites
    - `web-add` to scrape [open-directories](https://old.reddit.com/r/opendirectories/)
