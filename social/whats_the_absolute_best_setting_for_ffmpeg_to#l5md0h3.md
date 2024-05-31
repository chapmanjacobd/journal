Smallest would probably need to be scene by scene. You can use this https://github.com/master-of-zen/Av1an with `libsvtav1`

If you don't want to use that just stick with a preset:

- https://trac.ffmpeg.org/wiki/Encode/AV1#Presetsandtunes
- https://gitlab.com/AOMediaCodec/SVT-AV1/-/blob/master/Docs/Ffmpeg.md#most-common-options

Something like `-c:v libsvtav1 -preset 2 -crf 40` would be a configuration which wants to minimize filesize and not care about encode time

> small as i can make them with practically no visual difference vs the raw bluray

AV1 is amazing but I don't think this is technically possible. Even with the same bitrate as blu-ray, the codec characteristics will be different. H.264 makes more sense for Blu-Ray quality transcodes. 

> arc a380

Also, GPU encodes are seen as significantly worse than CPU in terms of quality and compression ratio. They are faster though... so it sounds like you might actually care about encode-time? In that case a preset of 6 or 8 might be better
