Btrfs checksumming helps you know when your data has become corrupted in ways that the HDD Firmware was unable to detect (bitflips which escape the drive's internal ECC) which would otherwise be silent corruption.

To check HDD hardware status rely on SMART. To check for silent corruption rely on checksums. 

If checksums are failing you need to think holistically--silent corruption can come from cables, RAM, or any other part of the system. Once the bits are passed off to the HDD it is the responsibility of the HDD hardware / firmware.

https://louwrentius.com/what-home-nas-builders-should-understand-about-silent-data-corruption.html

If you don't have regular and tested backups then you should make one the minute you see `Offline_Uncorrectable`. It means your drive is [on the way out](https://en.wikipedia.org/wiki/Bathtub_curve). 

If your drive gets any Offline_Uncorrectable errors it is likely that it will get more errors soon. When the spare sector pool is depleted, any Offline_Uncorrectable errors you get afterwards won't be able to be remapped to new space within the drive. This means that from that point, any time you write something to those bad sectors (and any new ones after) you are effectively throwing away data--even if you re-partition or re-format the disk. The hardware is the issue.

At that point, btrfs can still tell you about checksum mismatches but the disk is not very useful for writing. If the disk doesn't reliably write data then even with dupe metadata the likelihood of filesystem corruption increases (any filesystem--not just btrfs). Depending on the source of the Offline_Uncorrectable errors it is also likely that the disk won't be any good at reading data too. Write and read errors generally go hand in hand.

> It fails the short test and long test

This should signal alarm bells to you. If a drive fails a short / conveyance test that usually means something is very wrong.
