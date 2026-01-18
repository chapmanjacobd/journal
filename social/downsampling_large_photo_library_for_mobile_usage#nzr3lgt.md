maybe something like this?

    mogrify -path ./resized -resize 2000x2000 *.jpg
    exiftool -overwrite_original -tagsFromFile %d/../%f.%e -all:all -unsafe -FileModifyDate ./resized/

You'll probably want to preserve whatever the original file type was as some tags are only valid on Tiff vs Jpg, etc
