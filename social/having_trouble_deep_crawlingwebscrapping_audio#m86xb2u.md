There are ID3 tags, at least for some files:

    $ ffprobe https://www.russian-records.com/data/media/7/Strok-Serdce.mp3
    [mp3 @ 0x5619218090c0] Estimating duration from bitrate, this may be inaccurate
    Input #0, mp3, from 'https://www.russian-records.com/data/media/7/Strok-Serdce.mp3':
      Metadata:
        track           : 2
        artist          : Строк Оскар
        title           : Сердце матери
        album           : Adler Elektro №7441
        comment         : август
        composer        : (Жак Еллен, Лу Поллак - Оскар Строк)
        publisher       : Германия
        date            : 1930
      Duration: 00:03:10.41, start: 0.000000, bitrate: 128 kb/s
      Stream #0:0: Audio: mp3 (mp3float), 44100 Hz, mono, fltp, 128 kb/s

You can use my CLI tool to import this information to a sqlite database without needing to download everything:

    pip install library
    library webadd --audio russian-records.db https://www.russian-records.com/data/media/ -v

edit: okay yeah a lot doesn't have metadata... hmm...
