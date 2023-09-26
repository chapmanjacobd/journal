if you use fish shell this is pretty easy:

    cat ./dl-instagram.fish
    gallery-dl $argv
    or yt-dlp $argv

Here's a more complex example, alternative way using $status: https://github.com/chapmanjacobd/computer/blob/adc6c6da3df2a9c293f6ff6852e1d44d73988b7e/.config/fish/functions/dl-get-photos.fish but I don't use that function any more because I've found it is better to just be explicit about whether you want an image or video because both gallery-dl and yt-dlp can do both (thumbnail only, or calling yt-dlp from gallery-dl)
