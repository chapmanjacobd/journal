It's still a *baby* tool so don't expect it to replace the [OG](## "original gangster") ODScanner.

The main benefit is that it uses ffprobe (video and audio) and exifTool (image) to get additional metadata that other tools might not bubble up. You can then filter out using this metadata and print matching URLs or download.

https://github.com/chapmanjacobd/library#webadd

You can use it like this:

    pip install xklb
    library webadd --fs open_dir.db URL # default if no profile flag, only basic metadata
    library webadd --video open_dir_video.db URL
    library webadd --audio open_dir_audio.db URL
    library webadd --image open_dir_image.db URL

After scanning you can download like this:

    library download open_dir.db --fs --prefix ~/d/dump/video/ -v

Or stream directly to `mpv`:

    library watch open_dir.db
    library watch open_dir.db --random
    library watch open_dir.db --sort size/duration desc
    library watch open_dir.db -h  # there are many, many options

### Some interesting options:

#### Duration

    -d+3min   # only include video or audio with duration greater than 3 minutes
    -d-3min   # only include video or audio with duration lesser than 3 minutes

#### Search

    -s 'search string'  # only include URLs which link text or paths match the query

#### Media metadata

    -w "width >= 1280"  # only include video with resolution bigger than 1280px wide
    -w "fps >= 48"  # only include weird frames per second video
    -w "audio_count >= 2"  # only include video with 2 or more audio tracks
    -w "subtitle_count >= 1"  # only include video with 1 or more subtitle tracks
    -w "size > $(numfmt --from=iec 1M)"  # only include files larger than 1 MiB

#### Printing

    -p   # prints a table instead of downloading
    -p f # prints a pipeable list of URLs
    -p d # marks URLs as deleted (the next time download is run it will skip those URLs)

### other xklb subcommands

You can also use `lb du open_dir.db` to estimate folder sizes as well as many other xklb subcommands:

    lb du /tmp/tmp.1jhlFdZcbf.db
    path                           size    count
    ------------------------  ---------  -------
    https://unli.xyz/p/2016/  619.5 MiB       31
    https://unli.xyz/p/2017/   70.6 MiB        9
    https://unli.xyz/p/2021/    1.5 MiB        3
    https://unli.xyz/p/2015/    8.3 MiB       27
    https://unli.xyz/p/2018/    1.7 MiB        8
    https://unli.xyz/p/2019/  124.9 KiB        3
    https://unli.xyz/p/2020/    1.4 KiB        4
    https://unli.xyz/p/2022/  220 Bytes        1
    8 paths at current depth (8 folders, 0 files)

File tree depth is configurable:

    lb du /tmp/tmp.1jhlFdZcbf.db --depth=6
    path                                                                                size    count
    -----------------------------------------------------------------------------  ---------  -------
    https://unli.xyz/p/2017/ivatan.pptx                                             36.3 MiB
    https://unli.xyz/p/2017/Untitled 2.ogg                                          31.5 MiB
    https://unli.xyz/p/2016/fuguestate/                                            617.8 MiB       28
    https://unli.xyz/p/2017/zIES-interculturaleffectiveness.pdf                      1.9 MiB
    https://unli.xyz/p/2021/everydayvirtualvacation.ics                              1.5 MiB
    https://unli.xyz/p/2016/ABTAME.pdf                                               1.0 MiB
    https://unli.xyz/p/2018/uwf-manual.pdf                                         841.5 KiB
    https://unli.xyz/p/2017/networkpro.pdf                                         798.3 KiB
    https://unli.xyz/p/2018/Applied Anthropology Project Report.pdf                715.4 KiB
    https://unli.xyz/p/2016/humancapital.pdf                                       566.0 KiB
    https://unli.xyz/p/2015/5 collection/                                            8.3 MiB       27
    https://unli.xyz/p/2018/vacationplanner.ods                                    140.1 KiB
    https://unli.xyz/p/2017/zSILENCE_Chapter_Eight Aug 6 2012 revision b.doc        76.5 KiB
    https://unli.xyz/p/2019/anth310_final.pdf                                       73.8 KiB
    https://unli.xyz/p/2016/MacArthur.pdf                                           55.2 KiB
    https://unli.xyz/p/2017/zjesserichmond_TranscriptofInterviewwithJohn.docx.pdf   51.1 KiB
    https://unli.xyz/p/2019/it491-research.pdf                                      50.6 KiB
    https://unli.xyz/p/2017/YC_alt.cinema.pdf                                       25.8 KiB
    https://unli.xyz/p/2018/fall.2018.hw.ods                                        25.6 KiB
    https://unli.xyz/p/2017/What would you do.pdf                                    6.8 KiB
    https://unli.xyz/p/2018/travelplannerv0/                                         9.0 KiB        4
    https://unli.xyz/p/2017/money.txt                                              625 Bytes
    https://unli.xyz/p/2020/city_explorer.html                                     624 Bytes
    https://unli.xyz/p/2019/travelplanner.html                                     463 Bytes
    https://unli.xyz/p/2021/everydayvirtualvacation.html                           389 Bytes
    https://unli.xyz/p/2020/reverse_flight_search.html                             328 Bytes
    https://unli.xyz/p/2020/tabsender.html                                         275 Bytes
    https://unli.xyz/p/2021/city_calc.html                                         275 Bytes
    https://unli.xyz/p/2020/proliferation.html                                     238 Bytes
    https://unli.xyz/p/2022/library.html                                           220 Bytes
    30 paths at current depth (3 folders, 27 files)

#### extra pro-tip***

If you use Linux / fish shell this might be helpful:

    function tempdb
        mktemp --suffix .db | tee /dev/tty
    end

then you can do `lb webadd (tempdb) URL` for example and it will save to a temporary database and print the local path of that database before running the scanner.
