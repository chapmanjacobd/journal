> I would rather get rid of every second frame than reduce the resolution

If anyone wants to do something like this, using a bitstream filter in ffmpeg is very fast if your source codec supports it. For example this will only include keyframes in the output:

    -c:v copy -bsf:v noise=drop=not(key)
