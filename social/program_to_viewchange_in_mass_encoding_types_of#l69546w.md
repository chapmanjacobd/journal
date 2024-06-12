Similar to encoding checker there are a couple libraries out there which use file data to determine encoding. One of them is https://github.com/cdgriffith/puremagic

You can efficiently run puremagic over millions of files and save the most likely result:

    pip install xklb
    lb fsadd --fs fs.db .\folder1\ .\folder2\

The puremagic info is saved as filetype
