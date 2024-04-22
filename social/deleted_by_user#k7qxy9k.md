If the working directory is the external storage folder then the frames will be saved there unless you specify the absolute or relative path to a different location. For example:

    ffmpeg -ss 00:00 -i filefour.mkv -t 02:20:06 /sdcard/frame%05d.png
