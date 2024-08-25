I think it's probably best to write something that you know well because you built it yourself. But I wrote something that might help. Here's what I would do first:

Scan for file types

    fd -tf -HI | awk -F'.' '{print $NF}' | sort | uniq -c | sort -g

(if you are on Windows you can do `scoop install msys2 fd nushell`. With nushell you don't need sort before uniq. This should work: `fd -tf -HI | awk -F'.' '{print $NF}' | lines | uniq -c | sort`)

Then you can run this script to move only the specific files by filetype into a different location but preserve the existing folder hierarchy:

    pip install xklb
    library mv --ext jpg,png ./drive1/ ./drive2/Pictures/

Or scan and move filtering on duration:

    library fsadd vids.db --video ./drive1/
    library fs vids.db -d-5 -d+30 -pf | library relmv - ./drive2/

That will move videos between 5 and 30 minutes in length to the drive2 folder. 

When you are moving a list of files use `library relmv`. When merging folders use `library mv`
