I like SpaceSniffer, WizTree, and QDirStat. 

I know for sure that you can export and import file lists in SpaceSniffer and QDirStat--[looks like WizTree can also do it](https://diskanalyzer.com/guide)

I wrote some software that can also do this: 

    pip install xklb
    lb fsadd --filesystem filelists.db D:/

Then when you need to update the list just do 

    lb fsupdate filelists.db

And you can browse the lists in the browser via datasette:

    pip install datasette
    datasette filelists.db
