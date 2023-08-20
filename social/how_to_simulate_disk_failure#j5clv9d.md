> I wouldn't count on anything larger than a few kB being accessible

why is that so ? does that mean only files stored with inline extents are accessible in a degraded `single` scenario? 

There is no striping so I would expect that, as long as files are small enough to be stored in a single 1gb block and/or the blocks for that data are all stored on a drive which didn't fail, then they should be accessible.

I have 8 disks and 3 partial backups (just the important files: 2 offsite, 1 onsite). I would be okay with 25% or even 50% data loss if one disk failed (that is to say one disk had fragments on it for 4 disks-worth of files) but it would be dissappointing to have 99% data loss
