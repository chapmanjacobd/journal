I've invested a significant amount of time in solving this type of problem. I wrote two scripts which can be used to merge folders. Including file over file, file over folder, and folder over file conflicts.

    pip install xklb
    lb mv -h

    usage: library merge-mv SOURCE ... DEST [--simulate] [--ext EXT]
    
        By default it won't matter if source folders end with a path separator or not
    
            library merge-mv folder1  folder2/  # folder1 will be merged with folder2/
            library merge-mv folder1/ folder2/  # folder1 will be merged with folder2/
    
        --bsd mode: an ending path separator determines if each source is to be placed within or merged with the destination
    
            library merge-mv --bsd folder1/ folder2/  # folder1 will be merged with folder2/
            library merge-mv --bsd folder1  folder2/  # folder1 will be moved to folder2/folder1/
    
        --parent mode: always include the parent folder name when merging
    
            library merge-mv --parent folder1  folder2/  # folder1 will be moved to folder2/folder1/
            library merge-mv --parent folder1/ folder2/  # folder1 will be moved to folder2/folder1/
            library merge-mv --parent file1.txt folder2/ # file1 will be moved to folder2/file1_parent_folder/file1.txt
    
        nb. This tool, like other library subcommands, only works on files. Empty folders will not be moved to the destination
    
    positional arguments:
      DESTINATION         Destination directory
        STRING
    
    options:
      --copy (-c)         Copy instead of move
      --modify-depth      Trim path parts from each source
      (-mD)
        STRING
      --sizes (-S)        Constrain media to file sizes (uses the same syntax as
        STRING            fd-find)
                          -S 6           # 6 MB exactly (not likely)
                          -S-6           # less than 6 MB
                          -S+6           # more than 6 MB
                          -S 6%10       # 6 MB ±10 percent (between 5 and 7 MB)
                          -S+5GB -S-7GB  # between 5 and 7 GB
      --no-url-decode     Skip URL-decoding/unquoting when printing URLs
    
    Replace Files:
      --bsd               BSD trailing slash behavior
      --parent            Include parent (dirname) when merging
      --file-over-file    Specify the conflict resolution strategy for file on file
        [action-if ...]   clobbering
      fallback
                          In this scenario you have a file with the same name as a
                          file in the target directory:
    
                          file1.zip (existing file)
                          file1.zip (incoming file)
    
                          Choose ZERO OR MORE of the following options:
                            delete-dest-hash     will delete the existing file if
                          the SHA-256 hash matches
                            delete-dest-size     will delete the existing file if
                          the file size matches
                            delete-dest-larger   will delete the existing file if it
                          is larger
                            delete-dest-smaller  will delete the existing file if it
                          is smaller
    
                            If you trust your target is more recent than the
                          source(s):
                            delete-src-hash      will delete the incoming file if
                          the SHA-256 file hash matches
                            delete-src-size      will delete the incoming file if
                          the file size matches
                            delete-src-larger    will delete the incoming file if it
                          is larger
                            delete-src-smaller   will delete the incoming file if it
                          is smaller
    
                          Choose ONE of the following required fallback options:
                            skip             will skip the incoming file
                            rename-dest      will rename the existing file to
                          file1_1.zip
                            delete-dest      will delete the existing file
                            delete-dest-ask  will delete the existing file if
                          confirmed for the specific file
    
                            If you trust your target is more recent than the
                          source(s):
                            rename-src       will rename the incoming file to
                          file1_1.zip
                            delete-src       will delete the incoming file
    
                          If you use both an delete-src* option and an delete-dest*
                          option then BOTH src and dest could be deleted! (default:
                          "delete-src-hash rename-dest")
      --file-over-folder  Specify the conflict resolution strategy for file on
        {skip rename-src  folder clobbering
      rename-dest
      delete-src          In this scenario you have a file with the same name as a
      delete-dest merge}  folder in the target directory:
    
                          folder1.zip/ (existing folder)
                          folder1.zip  (incoming file)
    
                          Choose ONE of the following options:
                            skip         will skip the incoming file
                            rename-src   will rename the incoming file to
                          folder1_1.zip
                            rename-dest  will rename the existing folder to
                          folder1_1.zip/
                            delete-src   will delete the incoming file
                            delete-dest  will delete the existing folder tree
                            merge        will move the incoming file to
                          folder1.zip/folder1.zip (default: "merge")
      --folder-over-file  Specify the conflict resolution strategy for folder on
        {skip             file clobbering
      rename-dest
      delete-src          In this scenario you have a file with the same name as a
      delete-dest merge}  folder somewhere in the target folder hierarchy:
    
                          en.wikipedia.org/wiki                       (existing
                          file)
                          en.wikipedia.org/wiki/Telescopes/index.html (incoming
                          folder + files)
    
                          Choose ONE of the following options:
                            skip         will skip the incoming files within wiki/
                            rename-dest  will rename the existing file to wiki_1
                            delete-src   will delete the incoming folder tree
                            delete-dest  will delete the existing file
                            merge        will move the existing file to
                          en.wikipedia.org/wiki/wiki (default: "merge")
    
    Global options:
      --verbose (-v)      Control the level of logging verbosity
                          -v     # info
                          -vv    # debug
                          -vvv   # debug, with SQL query printing
                          -vvvv  # debug, with external libraries logging (default:
                          0)
      --no-pdb            Exit immediately on error. Never launch debugger
      --timeout (-T)      Quit after N minutes
        TIME
      --timeout-size      Quit after processing N bytes
      (-TS)
        SIZE
      --threads           Load N files in parallel
        INTEGER
      --same-file-thread  Read the same file N times in parallel (default: 1)
      s
        INTEGER
      --ext (-e)          Include only specific file extensions
        STRING
      --simulate


The other one is more complicated code but will allow you to see conflicts before moving any files:

    lb merge-folders -h

However, it doesn't support the clobbering configuration that `lb mv` does. 

`lb relmv` is also useful if you want to move individual files and preserve the file hierarchy
