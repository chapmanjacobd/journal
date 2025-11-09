I recommend running the numbers for yourself...

    Type           Drive Price  Disk Price  Disk Size  Disk Price/TB  Max Disks  Total Size  Disk Cost  Total Cost  Price/TB  200 TB Price/TB  400 TB Price/TB  600 TB Price/TB
    -------------  -----------  ----------  ---------  -------------  ---------  ----------  ---------  ----------  --------  ---------------  ---------------  ---------------
    LTO-7          2985         48          6          8              64         384         3072       $6,057      $15.77    $22.93           $15.46           $12.98
    LTO-8          3200         64          12         5.333333333    32         384         2048       $5,248      $13.67    $21.33           $13.33           $10.67
    LTO-9          4894         98          18         5.444444444    16         288         1568       $6,462      $22.44    $29.91           $17.68           $13.60
    SuperLoader 3  7767         98          18         5.444444444    6          288         588        $8,355      $29.01    $44.28           $24.86           $18.39
    NAS            1220         380         26         14.61538462    10         260         3800       $5,020      $19.31    $20.72           $17.67           $16.65
    NAS as Tape    1220         255         20         12.75          19         380         4845       $6,065      $15.96    $18.85           $15.80           $14.78

(the "NAS as Tape" option is getting a 10-disk QNAP and swapping out disks manually as needed, as if they were tapes)

It doesn't make sense at all... especially if you factor in the unexpected maintenance costs and learning curve which is a bit higher than hot-swapping SAS drives (and when things go wrong much higher learning curve--either get out your soldering iron or get out your wallet for another tape drive), much much less random read performance, and running on low write buffer can quickly degrade a tape, etc.

That being said... this doesn't factor in electricity costs. If you live somewhere where 1 kWh is $0.40 or something then maybe tape starts to make sense just because it is 0 watts at rest... or maybe the NAS as Tape option would also be good if you can get by without an autoloader
