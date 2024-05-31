> at the same bitrate

The artifacts are _different_ from what x264 might produce at the same bitrate, which is why people find newer codecs more acceptable for lower bitrates. 

But for higher bitrates, yes, I would say that AV1 are not designed to capture the same quality profile as something like H.264 and AV1 would have more noticeable artifacts at the same high bitrates unless you disable [some of the advanced encoding features](https://gitlab.com/AOMediaCodec/SVT-AV1/-/blob/master/Docs/Parameters.md#rate-control-options) to make the algorithm behave a bit more like H.264. AV1, H.264, (and Opus) are all very versatile codecs (at least in theory--it also depends on the specific implementation), but you would want to disable some of the more aggressive [filters](https://hacks.mozilla.org/2018/06/av1-next-generation-video-the-constrained-directional-enhancement-filter/) to have comparable artifacts as H.264 but at that point you may as well use H.264.
