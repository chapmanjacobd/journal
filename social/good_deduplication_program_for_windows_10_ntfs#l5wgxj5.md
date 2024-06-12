This might seem complicated, but I promise that it is fast. Even faster than rmlint if most of your files are bigger than 5MB. It takes less than an hour to rescan 80TB where rmlint would take several days:

- pip install xklb pandas
- lb fsadd --fs data.db .\folders\
- lb dedupe-media --fs data.db --dedupe-cmd "custom script for hardlinking"

You can run this without a custom dedupe-cmd but press enter without typing "y" when it prompts you to delete duplicates. You'll still be able to manually look at duplicates with the CSV file that it shows the location of.

Otherwise, you'll need to write a batch script that takes in two parameters: $1 is the duplicate file and $2 is the original. This is the same interface that rmlint uses for compatibility purposes (the script itself doesn't use rmlint).

For mergerfs+btrfs reflinks you can use: `--dedupe-cmd` [dupreplace.fish](https://github.com/chapmanjacobd/computer/blob/main/bin/dupreplace.fish)
