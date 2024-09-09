I found this guide earlier which might help: https://slhck.info/video/2017/02/24/vbr-settings.html

If `-crf 20` was too low quality you could try `-b:v 0 -crf 10`. crf is the main lever you have to control quality vs file size. `-qmin`, `-qmax`, `-maxrate` can help with fine-tuning once you are in the right ballpark.

Also take a look at: https://slhck.info/video/2017/03/01/rate-control.html Whichever rate-control mode you choose, the results will be pretty similar. CRF is the easiest to control, has good encoding time tradeoffs and it can deliver archive quality results. But the person at that site also recommends Two-pass ABR when Encoding for Devices, which would look like:

    ffmpeg -i <input> -c:v libvpx -b:v 1M -pass 1 -f null /dev/null
    ffmpeg -i <input> -c:v libvpx -b:v 1M -pass 2 <output>.webm

But honestly I don't think it is worth it unless you are Netflix or something (the encoding time will effectively double). Better to fiddle around with the `-crf` and choose a value between `0` and `63`. If `-crf 10` is good quality but too big then try `15`

> -crf 20 was already set

make sure you don't have -b:v in your command twice, and in ffmpeg the order of arguments matters a lot. the `-b:v` needs to go after the `-i` input file and before the output filename
