docker exec -it $(docker container ls -l | tail -1 | cut -f1 -d' ') /bin/bash

docker logs -f $(docker container ls -l | tail -1 | cut -f1 -d' ')

toolbox apt update && toolbox apt install -y sysstat iftop ncdu lsof htop kitty-terminfo

toolbox ncdu /media/root/mnt/stateful_partition/var/lib/docker/overlay2

