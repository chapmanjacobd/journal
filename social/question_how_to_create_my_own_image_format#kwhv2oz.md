> The only thing that I don't know is how images are decoded

All data that can be decoded must have been encoded first. Think compression: compress --> decompress (this analogy works because compression _is_ a type of coding: "source coding"). Codings are simply formalized transformations of data. 

Formats or codec (enCODE-DECode) are simply formal coding specifications. Coding as in information theory and not as in software writing.

https://en.wikipedia.org/wiki/Coding_theory

For images specifically, here are some high quality resources:

- [QOI — The Quite OK Image Format](https://qoiformat.org/)
 - The spec is only [one page](https://qoiformat.org/qoi-specification.pdf) long! Amazing! 
- [BranchEducation How are Images Compressed?  [46MB ↘↘ 4.07MB] JPEG In Depth](https://www.youtube.com/watch?v=Kv1Hiv3ox8I)

And for ffmpeg specifically... try compiling ffmpeg from source first. Then take a look at [how QOI support is integrated](https://github.com/FFmpeg/FFmpeg/commit/973fab565378cbdd0712977152a66f5b17938d51). From there it should be somewhat clear how you can add your own and recompile.

- https://github.com/phoboslab/qoi/blob/master/qoi.h
- https://github.com/FFmpeg/FFmpeg/commit/973fab565378cbdd0712977152a66f5b17938d51
