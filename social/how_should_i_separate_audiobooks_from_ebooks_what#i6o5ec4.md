I only organize at the top level. I used to try to keep music organized with subfolders but I no longer bother with that.

I have up to 100 root level folders, but there could be more if you are fine with duplicating numbers for less frequently used folders (ie. 42\_GameCube and 42\_Wii). 

I'm only using 64 root level folders right now. This looks like:

    00_Metadata*
    02_Home*
    05_Car*
    20_Spatial
    21_Raster
    22_Vector
    30_Computing*
    31_Downloads*
    39_Backups
    50_eBooks*
    51_Manga
    55_Unsorted_Documents
    59_Library
    70_Now_Watching*
    79_Library
    80_Now_Listening*
    81_New_Music
    82_Audiobooks
    85_Inspiration
    etc


\* denotes folders synced with syncthing to all my computers and phone. 

I keep a 400GB card in my phone but sometimes files in 31\_Downloads can get quite big--but this is not usually an issue. 

It means I can sort files once, whether on my phone or my laptop or my desktop and the changes will get synced and I only need to organize files once (for folders too large to sync I have subfolders in the synced folders to denote actions that the desktop can do, for example a "keep" subfolder to denote moving a video to the video library folder--there is a script that runs on the desktop which runs periodically to keep everything organized). 

I make heavy use of stignore. If you try to replicate my setup be careful and do some tests with syncthing first because it can delete files in ways you might not expect if you don't use stignore correctly. I recommend using Simple Trash can versioning so you can undelete accidentally deleted files easily until you trust syncthing and know how decentralized sync behaves.


I also use btrfs to take snapshots and fd-find+rmlint to quickly scan for duplicate files.
