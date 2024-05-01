I wrote a small wrapper around exiftool: https://github.com/chapmanjacobd/library

You can use it like this:

    $ lb fsadd --image photos.db ./folder1/ ./folder2/

Remove duplicates:

    $ lb dedup-files --fs photos.db

Print CSV sorted by time_modified

    $ lb fs photos.db -u time_modified -pf --cols path,time_modified

Print 10,000 paths sorted by time_modified

    $ lb fs photos.db -u time_modified -L 10000 -pf

But if you already are familiar with Excel using plain exiftool and a CSV might be easier

For sorting or deleting files I can recommend:

CLI: 

- https://old.reddit.com/r/DataHoarder/comments/1c2vcug/software_for_managing_own_videos/kzey3zn/?context=3
- feh (Linux/BSD only) 

GUI:

- ACDSee (Windows only)
- Darktable culling mode
- cbird https://github.com/scrubbbbs/cbird

For similar images deduping try: DupeGuru, Czkawka, cbird, or "Visual Similarity Duplicate Image Finder" (Windows only)
