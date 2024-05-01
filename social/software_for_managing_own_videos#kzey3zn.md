If you are handy with the command line I wrote a tool that might help. I use multiple-playback mode often to sort videos into different folders or delete them:

    pip install xklb
    lb fsadd 2003.db ./unsorted_2003_folder/

This will read in all the video files from the folder into a sqlite database which you can reuse with various commands, such as:

    lb watch 2003.db --multiple-playback 4 --sort time_created desc --loop -i \
         --cmd5 'mv {} ./2003/aunt_selma/' \
         --cmd6 'mv {} ./2003/uncle_tonk/'

This will launch 4 videos at once then you can press a bound key in mpv to exit 5 or exit 6 and that will trigger xklb to move the file into the specific folder. A bit hacky but very flexible

`feh` offers a similar interface for images, although you can view images in mpv too.
