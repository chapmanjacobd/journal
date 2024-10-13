> millions of tiny files like Node_modules files

I would probably use rmlint if you are just looking to remove duplicates

But for merging folders I wrote a program which allows for granular control when encountering file on file and other types of path conflicts. By default it will check that the files are the same and delete the source if the target already matches the SHA-256. If no match then it will rename the existing file to X_1.ext and move the source file to the destination.

    $ library mv -h
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
    
    positional arguments:
      DESTINATION                   Destination directory
        STRING
    
    options:
      --copy (-c)                   Copy instead of move
      --modify-depth (-mD)          Trim path parts from each source
        STRING
      --sizes (-S)                  Constrain media to file sizes (uses the same syntax as fd-find)
        STRING                      -S 6           # 6 MB exactly (not likely)
                                    -S-6           # less than 6 MB
                                    -S+6           # more than 6 MB
                                    -S 6%10       # 6 MB ±10 percent (between 5 and 7 MB)
                                    -S+5GB -S-7GB  # between 5 and 7 GB
      --no-url-decode               Skip URL-decoding/unquoting when printing URLs
    
    Replace Files:
      --file-over-file              Specify the conflict resolution strategy for file on file clobbering
        [action-if ...] fallback
                                    In this scenario you have a file with the same name as a file in the target
                                    directory:
    
                                    file1.zip (existing file)
                                    file1.zip (incoming file)
    
                                    Choose ZERO OR MORE of the following options:
                                      delete-dest-hash     will delete the existing file if the SHA-256 hash matches
                                      delete-dest-size     will delete the existing file if the file size matches
                                      delete-dest-larger   will delete the existing file if it is larger
                                      delete-dest-smaller  will delete the existing file if it is smaller
    
                                      If you trust your target is more recent than the source(s):
                                      delete-src-hash      will delete the incoming file if the SHA-256 file hash
                                    matches
                                      delete-src-size      will delete the incoming file if the file size matches
                                      delete-src-larger    will delete the incoming file if it is larger
                                      delete-src-smaller   will delete the incoming file if it is smaller
    
                                    Choose ONE of the following required fallback options:
                                      skip             will skip the incoming file
                                      rename-dest      will rename the existing file to file1_1.zip
                                      delete-dest      will delete the existing file
                                      delete-dest-ask  will delete the existing file if confirmed for the specific
                                    file
    
                                      If you trust your target is more recent than the source(s):
                                      rename-src       will rename the incoming file to file1_1.zip
                                      delete-src       will delete the incoming file
    
                                    If you use both an delete-src* option and an delete-dest* option then BOTH src and
                                    dest could be deleted! (default: "delete-src-hash rename-dest")
      --file-over-folder            Specify the conflict resolution strategy for file on folder clobbering
        {skip rename-src
      rename-dest delete-src        In this scenario you have a file with the same name as a folder in the target
      delete-dest merge}            directory:
    
                                    folder1.zip/ (existing folder)
                                    folder1.zip  (incoming file)
    
                                    Choose ONE of the following options:
                                      skip         will skip the incoming file
                                      rename-src   will rename the incoming file to folder1_1.zip
                                      rename-dest  will rename the existing folder to folder1_1.zip/
                                      delete-src   will delete the incoming file
                                      delete-dest  will delete the existing folder tree
                                      merge        will move the incoming file to folder1.zip/folder1.zip (default:
                                    "merge")
      --folder-over-file            Specify the conflict resolution strategy for folder on file clobbering
        {skip rename-dest
      delete-src delete-dest        In this scenario you have a file with the same name as a folder somewhere in the
      merge}                        target folder hierarchy:
    
                                    en.wikipedia.org/wiki                       (existing file)
                                    en.wikipedia.org/wiki/Telescopes/index.html (incoming folder + files)
    
                                    Choose ONE of the following options:
                                      skip         will skip the incoming files within wiki/
                                      rename-dest  will rename the existing file to wiki_1
                                      delete-src   will delete the incoming folder tree
                                      delete-dest  will delete the existing file
                                      merge        will move the existing file to en.wikipedia.org/wiki/wiki (default:
                                    "merge")
      --skip-open                   Skip source files that are already open in another process
      --bsd                         BSD/rsync trailing slash behavior
      --parent                      Include parent (dirname) when merging
