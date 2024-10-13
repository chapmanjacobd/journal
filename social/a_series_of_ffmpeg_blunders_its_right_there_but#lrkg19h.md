open a non-admin PowerShell terminal. paste these to install:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

and then you can install ffmpeg:

    scoop install ffmpeg
