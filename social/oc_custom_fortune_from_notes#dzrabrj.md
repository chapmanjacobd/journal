I have a folder with many text files of my notes. I created this script to display 4 random lines from a random file every time I open a new terminal. sometimes it is out of context and funny, sometimes it is very useful

    function fish_greeting
      cat /proc/loadavg | cut -d' ' -f 2
      shuf -n 4 ~/drive/notes/(ls -p  ~/drive/notes/ |grep -v / | shuf -n 1) | cowsay -W 60 -f tux
    end

more photos
https://imgur.com/a/ylUufu6

edit: also here is .Xresources if interested:

    *background:  #ead7bb
    *foreground:  #000000
    *color0:  #291600
    *color1:  #ce2900
    *color2:  #397206
    *color3:  #ef6a00
    *color4:  #09272c
    *color5:  #d65c2a
    *color6:  #276640
    *color7:  #c8b9c2
    *color8:  #39260a
    *color9:  #e12300
    *color10:  #00892e
    *color11:  #e68300
    *color12:  #2d7d60
    *color13:  #eb652a
    *color14:  #759375
    *color15:  #8A5C62
    URxvt.perl-ext-common: default,matcher
    URxvt.url-launcher: /usr/bin/xdg-open
    URxvt.matcher.button: 1
    
