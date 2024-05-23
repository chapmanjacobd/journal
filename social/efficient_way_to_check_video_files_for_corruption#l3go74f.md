> but still play fine

Like you say, there are false positives but there are also false negatives with this command specifically. I spent a couple days playing around with ffmpeg and wrote up some of my findings here: https://github.com/qarmin/czkawka/discussions/721#discussioncomment-7944891

This is the command I use to quickly check a file for large corruption chunks (only takes about 1 second per file, to be more accurate you need to pay the cost of decoding more of the stream):

    $ pip install xklb
    $ library fsadd media.db --video --check-corrupt \
      --full-scan-if-corrupt 15% ./video/ -v

It does a quick scan and if more than 15% of the tests fail then it does a full scan which takes longer but is more accurate. The sqlite database has the results of the scan as a percentage of corruption

To only check one file at a time you can also use the media-check command directly: https://github.com/chapmanjacobd/library?tab=readme-ov-file#media-check
