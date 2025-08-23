# Common misconceptions

## VARIABLE=

`VARIABLE=` means VARIABLE is set to ""

`VARIABLE=` is not equivalent to an `unset VARIABLE`

## mv src vs mv src/

I feel like this is bad design if only because I didn't understand it until recently even after using Linux for over ten years.

tl;dr: what is the right way?

Well... it depends what you want to do. The program can't read your mind so I hope you read the manual well 🎃🏚️🎃

I think `mv` should be limited to tasks which don't change inodes. `cp` should probably error out similar to `mv` but I am 52 years and 10 days too late to provide my _deep_ and _useful_ insight /s.

`rsync`, despite doing different things based on trailing slash on `src` parameters, is more consistent from an operator perspective.

Put another way, limited to the below examples, these are the equivalent:

Nested one subfolder (actual destination `three/one/one`):

| Full Command                                     | Source Parameter | Destination Parameter |
| ------------------------------------------------ | ---------------- | --------------------- |
| `mv one three/one`                               | `one`            | `three/one`           |
| `cp -r one three/one && rm -rf one`              | `one`            | `three/one`           |
| `rsync -auh --remove-source-files one three/one` | `one`            | `three/one`           |
| `rclone move -q --no-traverse one three/one/one` | `one`            | `three/one/one`       |
| `library relmv one three/one` \*                 | `one`            | `three/one`           |

Merged subfolder (actual destination `three/one`):

| Full Command                                 | Source Parameter | Destination Parameter |
| -------------------------------------------- | ---------------- | --------------------- |
| `mv one/* three/one`                         | `one/*`          | `three/one`           |
| `cp -r one three && rm -rf one`              | `one`            | `three`               |
| `rsync -auh --remove-source-files one three` | `one`            | `three`               |
| `rclone move -q --no-traverse one three/one` | `one`            | `three/one`           |
| `library relmv one three` \*                 | `one`            | `three`               |

Merged destination (actual destination `three`):

| Full Command                                  | Source Parameter | Destination Parameter |
| --------------------------------------------- | ---------------- | --------------------- |
| `mv one/* three`                              | `one/*`          | `three`               |
| `cp -r one/* three && rm -rf one`             | `one/*`          | `three`               |
| `rsync -auh --remove-source-files one/ three` | `one/`           | `three`               |
| `rclone move -q --no-traverse one three`      | `one`            | `three`               |
| `library relmv one three` \*\*                | `one`            | `three`               |

I thought trailing slash mattered more, but it actually only matters in the "merged destination" instance.

Out of all of these, I think rclone provides the least surprising result. But rclone is a lot slower than `mv` in many scenarios and it should be noted that you can't rename files with `rclone` or `lb relmv` like you can with `mv`.

\* if no destination path parents are also named "one"

\*\* if any destination path parent is also named "one"

`library relmv` is an unusual case but I added it here because I was curious about the results. `relmv` preserves unique path data so each time you move a file the file will often gain more levels of nested folders. Given this property the results above are relatively tame. With [lb](https://github.com/chapmanjacobd/library) [relmv](https://github.com/chapmanjacobd/library/blob/main/xklb/scripts/relmv.py) it would only possible to end up with the merged destination if any of the parents of the destination folder were also named "one"--and in that case the other two end states would be impossible.

Setup:

    $ mkdir one three three/one
    $ touch one/(seq 1 5) three/one/(seq 5 10)

    $ tree
    .
    ├── one
    │   ├── 1
    │   ├── 2
    │   ├── 3
    │   ├── 4
    │   └── 5
    └── three
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 11 files

If a subdirectory with the same name exists, how will `mv` behave?

    $ mv one three
    $ mv one/ three   # equivalent
    $ mv one three/   # equivalent
    $ mv one/ three/  # equivalent
    mv: cannot move 'one' to 'three/one': Directory not empty

This will error, which is good. I'd rather see an error if my command was ambiguous.

All of these will be the same:

    $ mv one three/one
    $ mv one/ three/one      # equivalent
    $ mv one three/one/      # equivalent
    $ mv one/ three/one/     # equivalent
    $ mv one/ three/one/one  # equivalent
    $ tree
    .
    └── three
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            ├── 9
            └── one
                ├── 1
                ├── 2
                ├── 3
                ├── 4
                └── 5

    4 directories, 11 files

But the result is a bit might be a bit confusing if you are trying to move the items from inside the `one/` directory to the nested `one/` directory.

Especially because `cp` will act differently!!!!:

    $ cp -r one three
    $ cp -r one three/   # equivalent
    $ cp -r one/ three   # equivalent
    $ cp -r one/ three/  # equivalent
    $ tree
    .
    ├── one
    │   ├── 1
    │   ├── 2
    │   ├── 3
    │   ├── 4
    │   └── 5
    └── three
        └── one
            ├── 1
            ├── 10
            ├── 2
            ├── 3
            ├── 4
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 15 files

Just in case you are interested, these are different but justly so:

    $ cp -r one/ three/one
    $ cp -r one/ three/one/     # equivalent
    $ cp -r one/ three/one/one  # equivalent
    $ tree
    .
    ├── one
    │   ├── 1
    │   ├── 2
    │   ├── 3
    │   ├── 4
    │   └── 5
    └── three
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            ├── 9
            └── one
                ├── 1
                ├── 2
                ├── 3
                ├── 4
                └── 5

    5 directories, 16 files

To use `mv`, the normal solution here is to do this:

    $ mv one/* three/one

But this skips hidden files so you actually have to do this:

    $ mv one/* one/.* three/one

But your shell might abort early if you _don't_ have hidden files:

    mv one/* one/.* three/one
    fish: No matches for wildcard 'one/.*'. See `help wildcards-globbing`.
    command mv one/* one/.* three/one
                    ^~~~~^
    $ tree
    .
    ├── one
    │   ├── 1
    │   ├── 2
    │   ├── 3
    │   ├── 4
    │   └── 5
    └── three
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 11 files

Or it might run full speed ahead killdozer style:

    bash
    @$ mv one/* one/.* three/one
    mv: cannot stat 'one/.*': No such file or directory
    @$ tree
    .
    ├── one
    └── three
        └── one
            ├── 1
            ├── 10
            ├── 2
            ├── 3
            ├── 4
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 10 files

And don't even try to do this:

    $ mv one/. three/one
    mv: cannot move 'one/.' to 'three/one/.': Device or resource busy

But what about other tools?

### rsync src vs rsync src/

This is a little nuanced but more intuitive after you learn the small pattern

These two will both result in the same structure (only the slash on the source folder matters):

    $ rsync -auh --remove-source-files one three
    $ rsync -auh --remove-source-files one three/      # equivalent
    $ rsync -auh --remove-source-files one/ three/one  # equivalent
    $ tree
    .
    ├── one
    └── three
        └── one
            ├── 1
            ├── 10
            ├── 2
            ├── 3
            ├── 4
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 10 files

The slash on the source folder means that the source and destination should be merged rather than a subdirectory.

    $ rsync -auh --remove-source-files one/ three
    $ rsync -auh --remove-source-files one/ three/  # equivalent
    $ tree
    .
    ├── one
    └── three
        ├── 1
        ├── 2
        ├── 3
        ├── 4
        ├── 5
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 11 files

The only way to get a nested one/one/ folder is to do this:

    $ rsync -auh --remove-source-files one three/one
    $ rsync -auh --remove-source-files one three/one/  # equivalent
    $ tree
    .
    ├── one
    └── three
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            ├── 9
            └── one
                ├── 1
                ├── 2
                ├── 3
                ├── 4
                └── 5

    5 directories, 11 files

### rclone src vs rclone src/

    $ rclone move one three
    $ rclone move one three/
    $ rclone move one/ three
    $ rclone move one/ three/

These all result in:

    $ tree
    .
    ├── one
    └── three
        ├── 1
        ├── 2
        ├── 3
        ├── 4
        ├── 5
        └── one
            ├── 10
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 11 files

And this:

    $ rclone move one three/one
    $ rclone move one/ three/one
    $ rclone move one three/one/
    $ rclone move one/ three/one/
    $ tree
    .
    ├── one
    └── three
        └── one
            ├── 1
            ├── 10
            ├── 2
            ├── 3
            ├── 4
            ├── 5
            ├── 6
            ├── 7
            ├── 8
            └── 9

    4 directories, 10 files
