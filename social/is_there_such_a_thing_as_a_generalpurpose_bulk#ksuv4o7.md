There is not really a universal way of saving metadata to a file aside from file system (xattrs, etc)

ExifTool supports A LOT of file formats--I think it is the most generic tool given the breadth of support. You might also consider using sqlite3 via xklb fsadd and using a database editor to add a column for each thing you want to note
