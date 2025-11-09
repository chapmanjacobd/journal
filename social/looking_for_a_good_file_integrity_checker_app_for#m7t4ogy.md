I'm guessing you're on Windows. I recommend scoop. It handles installation to the PATH:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

    scoop install ffmpeg python
    pip install library

Yeah, there aren't any good tools that can batch fix arbitrary file formats. The biggest hindrance to this idea is that even for flipping a small number of bits this quickly turns into a brute-forcing-until-the-heat-death-of-the-universe problem--and this is really only possible for file formats which have some kind of quick block based checksum built-in or side channel (like torrents).

If you know ahead of time, you can generate parity files with par2 or snapraid... but after-the-fact is impossible for some file formats because there is no content checksum to verify against
