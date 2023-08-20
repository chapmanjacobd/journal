> Running out of meta data space will not cause transid errors

well the error messages are right next to each other--but they are almost an hour apart  

    sudo journalctl -t kernel \| tail -n +5782 \| head -226 > m/raidc3.txt

https://gist.github.com/chapmanjacobd/347ae53e057701dc39caa51ff3d6ee1d

    Jun 07 10:46:47 fedora kernel: BTRFS: error (device sdb) in \_\_btrfs\_free\_extent:3079: errno=-28 No space left
    Jun 07 10:46:47 fedora kernel: BTRFS info (device sdb): forced readonly
    Jun 07 10:46:47 fedora kernel: BTRFS: error (device sdb) in btrfs\_run\_delayed\_refs:2159: errno=-28 No space left
    Jun 07 11:32:17 fedora kernel: BTRFS error (device sdb): parent transid verify failed on 52440401969152 wanted 191436 found 191430
