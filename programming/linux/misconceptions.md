# Common misconceptions

## VARIABLE=

`VARIABLE=` means VARIABLE is set to ""

`VARIABLE=` is not equivalent to an `unset VARIABLE`

## mv src vs mv src/

I feel like this is bad design only because I didn't understand it until recently even after using Linux for over ten years.

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

This will error, which is good. I'd rather see an error if my command was ambiguous.

    $ mv one three
    mv: cannot move 'one' to 'three/one': Directory not empty

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
    $ rsync -auh --remove-source-files one three/
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
These are all the same:

    $ rsync -auh --remove-source-files one/ three
    $ rsync -auh --remove-source-files one/ three/
    $ rsync -auh --remove-source-files one/ three/one/
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

    $ rsync -auh --remove-source-files one three/one/
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
