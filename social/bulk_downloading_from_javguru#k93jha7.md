it's a command-line program which you can run on Windows, Mac, and Linux.

Here is a good introduction: https://www.youtube.com/watch?app=desktop&v=uwAqEzhyjtw

On Windows the above fish functions won't work unless you have WSL (Windows Subsystem for Linux), python 3.8 to 3.11, fish shell, and GNU Parallel. But I haven't tested the code on Windows or WSL very extensively. Because it requires the browser, I am more confident that the code will run outside of WSL on Windows.

Here are the non-WSL Windows setup instructions: https://github.com/chapmanjacobd/library/blob/main/.github/Windows.md

After that this should work:

    python -m xklb.scratch.javguru https://jav.guru/45176/dandy-368-wild-nature-heaven-vol-2-ai-uehara/

And then in PowerShell you could run a script like this to load a file with one URL per line and run sequentially

    $urls = Get-Content "url_file.txt"
    foreach ($url in $urls) {
      Invoke-Expression "python -m xklb.scratch.javguru $url"
    }

If it doesn't work, I'm sorry but you'll need to figure it out on your own. The difficult part was done for you already.
