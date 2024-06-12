`-tf` means type file. Since there aren't any other constraints this means ALL files, including in nested folders of the current working directory. If you just want the current top-level files add `--depth 1`

`-x` means execute

put the filename of your script

`{}` means the filepath that `fd` found. I think if you are only using `%1` then you don't actually need it but if you wanted to use `%2` for an output filename then you'd want to use `{} .\out\{/}` (for example). The docs are pretty easy to read: https://github.com/sharkdp/fd?tab=readme-ov-file#placeholder-syntax

edit: sorry I thought this was on the other post. Instead of my_script you can just do this:

    fd -tf -x ffmpeg -i {} -map 0:0 -map 0:1 -map 0:3 -c copy {}.en.mkv -map 0:0 -map 0:2 -map 0:4 -c copy {}.jp.mkv
