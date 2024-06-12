Whenever moving folders with folders which have the same names I would always wince when seeing "directory not empty" or "destination already exists" and then immediately give up and use a GUI file manager.

The existing solutions all have caveats:

    mv ./src/* ./dest/  

oops no dotfiles ?!

    rsync --remove-sent-files
    rclone move 

rsync and rclone will copy the files to move them which can be very slow when renaming is all that is needed

So I've created my own which uses BSD syntax:

    pip install xklb
    library merge-mv folder1  folder2/  # folder1 will go inside folder2
    library merge-mv folder1/ folder2/  # folder1 will be merged with folder2

nb. continuing the tradition of subtle caveats: my program won't move/copy empty directories because it only worries about files...

code: https://github.com/chapmanjacobd/library/blob/main/xklb/folders/merge_mv.py
