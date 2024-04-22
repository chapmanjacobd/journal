If you haven't renamed or moved your files I'm pretty sure you could run through everything again with the same command that you used to download only appending `--no-download-archive --embed-metadata`

If you don't have a list of links you could grab your IDs from download-archive by piping it through something like `grep youtube | sed 's|youtube |https://youtu.be/|'`
