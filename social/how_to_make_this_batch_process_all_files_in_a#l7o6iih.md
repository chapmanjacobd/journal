I think the easiest option for Windows is `fd-find`

https://github.com/sharkdp/fd?tab=readme-ov-file#on-windows

    fd -tf -x my_script {}

By default it will parallelize. To make things one file at a time you can set `-j 1` before `-x`

I think you could run this in parallel if you modify the script to use %~1 as part of the temporary filenames %~1.center.wav, etc? But if you aren't doing this often it's probably more trouble than it is worth
