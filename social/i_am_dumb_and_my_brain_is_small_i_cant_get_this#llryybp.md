try running this in non-admin powershell:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

Then you can run this in powershell, nushell, or cmd.exe:

    scoop install python
    python -m ensurepip
    pip install yt-dlp
