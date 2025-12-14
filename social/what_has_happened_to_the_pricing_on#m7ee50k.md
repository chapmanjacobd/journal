I like Tdarr but I also have a script that is working pretty well for me. If you like AVIF, AV1, Opus, and unzipped ePub:

    pip install library
    library shrink ./video/ ./audio/ ./comics/ ./rar_files/ ./zipped_media/

After a quick scan of everything in the folders it will calculate which files are worth compressing and ask to continue (use -y to skip the confirmation). You can tweak the compression cutoff via flags.
It will definitely degrade the quality! So test it out on a few copies of files before running it.
