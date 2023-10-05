> Shouldn't BTRFS also throw some errors, if SMART detects some issues?

Only for `Offline_Uncorrectable` errors if they happened during the time that the filesystem existed. If you reformatted the disk and filled it up again you would need for a `Offline_Uncorrectable` event to happen again.

Reporting a read error is what's supposed to happen if the drive can't read a sector. btrfs scrub compares data that was read with a stored CRC. But I don't know if these are mutually inclusive events.

> Modern hard drives feature an ability to recover from some read/write errors by internally remapping sectors and performing other forms of self-test and recovery. The process for this can sometimes take several seconds or (under heavy usage) minutes
> https://en.wikipedia.org/wiki/Error_recovery_control#Overview

This sector remapping is done transparently within the hard drive itself via the spare sector pool and is not exposed externally. So the hard drive won't reuse bad sectors if it believes that those sectors shouldn't be re-used. Errors like `Reallocated_Event_Count` / `Reallocated_Sector_Ct` / `UDMA_CRC_Error_Count` won't bubble up into btrfs because the HDD firmware has corrected the problem and so the state of the filesystem is unaffected by the error.

> When an error occurs when a sector is written the drive replaces the bad sector with a spare and then rewrites the data and there is no data loss. The "Reallocated Sectors Count" is a count of these sectors. But things aren't so simple when an error occurs when a sector is read. Remapping the sector would not be a good idea because this would prevent recovery of it's data if a later read operation were to succeed. Instead the drive makes a note of the bad sector and waits for one of 2 events to occur. The "Current Pending Sector Count" is a count of such sectors.

> 1. If the sector is later successfully read it can be remapped with no data loss. Unfortunately you have no way of knowing when this will occur or even if it is possible. The read operation may succeed at the next attempt or it may fail after 1000 tries.
> 2. If the sector is later written to it can be remapped with no data loss. Unfortunately there is no way of knowing when or if this will occur. If the sector contains frequently modified data the wait may not be long. But if the sector contains a system or application executable file it may be long time before it is updated, or it may not happen at all.

> https://superuser.com/questions/1269857/how-to-force-remap-current-pending-sector-count
