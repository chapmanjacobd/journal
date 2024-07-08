To be clear, to use `lb dedupe-media --fs` you'll need to run `lb fsadd --fs disk1.db .\folder1\ .\folder2\` first

But you can probably just use `lb mv` first and that will get rid of most duplicates if they have the same relative paths. That will be faster because it only needs to compare each file conflict with itself. Then do dedupe-media afterwards

But! dedupe-media can show you a CSV of all the duplicates before deleting any so that might be better. `lb mv` only has `--simulate` which will print linuxy psuedo commands that describe the actions it plans on taking one file at a time--and it doesn't go into specifics about file conflicts, that's what `lb merge-folders` is for...

edit: If you don't want to inspect everything one file at a time, something like this should work:

    library merge-mv --replace-same-hash src/ dest/   # this will merge+dedupe by removing file conflicts that are exact duplicates
    library merge-mv --rename-on-conflict src/ dest/  # any remaining file conflicts will be numerically named something like "_1.ext"
