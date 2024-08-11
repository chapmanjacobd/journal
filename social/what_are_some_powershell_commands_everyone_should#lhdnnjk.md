I put this together based on https://github.com/niedzielski/cb/blob/main/cb 

cb.bat works in cmd but requires `scoop install pasteboard`

    @echo off
    timeout 0 2>nul >nul
    if errorlevel 1 (
        clip
    ) else (
        pbpaste
    )

I guess in PowerShell you could do ?

    if ($Host.UI.RawUI.KeyAvailable) {
        Set-Clipboard
    } else {
        Get-Clipboard
    }

save that as cb.ps1 and then you can hopefully type `cb | sort.exe | cb`, etc
