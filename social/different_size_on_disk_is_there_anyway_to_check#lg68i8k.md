If those are sparse files you can compare actual size with apparent-size:

- https://github.com/chapmanjacobd/journal/blob/main/programming/linux/misconceptions.md#file-size
- `lb sample-hash` will print a warning when it encounters a sparse file but I guess this doesn't work on windows

Essentially this:

    function is_sparse_file
        set actual_size (du --block-size=1 "$argv" | awk '{print $1}')
        set apparent_size (du --block-size=1 --apparent-size "$argv" | awk '{print $1}')
    
        if test $actual_size -eq $apparent_size
            return 1
        else
            return 0
        end
    end
