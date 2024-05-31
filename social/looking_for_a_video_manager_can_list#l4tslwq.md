This is a good starting point: https://github.com/chapmanjacobd/library/blob/main/xklb/createdb/fs_add.py

It has `chapter_count`, `width`, `height`, `fps`, `subtitle_count`, `audio_count`, `language`, and it can very efficiently rescan directories. If you want to add additional metadata like container, video_format, audio_format, etc it shouldn't be too difficult: https://github.com/chapmanjacobd/library/blob/main/xklb/createdb/av.py
