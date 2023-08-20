I don't think this is true:

https://gist.github.com/chapmanjacobd/f65797ac957243873fd154f14bd53224

It appears that btrfs can recover from an anti-pair n-disk crash (as noted in the gist) BUT the caveat is that no metadata can be lost.

I don't know if btrfs guarantees that metadata pairing will always match data pairing:

ie. 4 disks

With `-m raid10 -d raid10` 

- `[(mA,dA),(mB,dB),(mA,dA),(mB,dB)]` you can lose (1,2),(1,4),(3,4)
- `[(mA,dA),(mA,dB),(mB,dA),(mB,dB)]` you can only lose (1,4),(2,3)

With `-m raid1 -d raid10`

- `[(m,dA),(dA),(dB),(m,dB)]` you can lose (1,3), (2,3), or (2,4)
- `[(dA),(m,dA),(dB),(m,dB)]` you can lose (1,3), (1,4), or (2,3)
- `[(dA),(dA),(m,dB),(m,dB)]` you can lose (1,3), (1,4), (2,3) or (2,4)

With `-m raid1c3 -d raid10`

- `[(dA),(m,dA),(m,dB),(m,dB)]` you can lose (1,3), (1,4), (2,3), or (2,4)

I'm not sure if btrfs is smart enough to choose `[(dA),(dA),(m,dB),(m,dB)]` every time. I think it only considers free space. If you are planning on using btrfs `-d raid10` with more than 1 drive failure you should store metadata at raid1c3 (or raid1c4 with 5+ drives)
