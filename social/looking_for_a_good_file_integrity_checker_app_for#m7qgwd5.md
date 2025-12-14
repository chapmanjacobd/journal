The most universal way would be to use checksums and compare before and after. Teracopy and rsync both support this.

I wrote a tool that can pretty reliably detect broken video and audio files via ffmpeg: https://github.com/qarmin/czkawka/discussions/721#discussioncomment-7944891 I haven't noticed any false positives with `--full-scan` but it does take a while. You can combine the quick scan option and full scan so that it doesn't waste time with the full scan when the file is likely fine:

    library mediacheck --full-scan-if-corrupt 20% ./videos/

You can add the flag `--delete-corrupt 25%` to delete files that are more than 25% corrupt. By default it will just print the results, one line per file.

> Also, if I were to convert the video to another format like .mp4, would that solve the problem, and would I lose any data during the process

Yes, this can help. You can also try flipping bits: https://github.com/anthwlock/untrunc
