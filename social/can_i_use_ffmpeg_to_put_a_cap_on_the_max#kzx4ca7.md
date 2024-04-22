The specific problem that you have might be better solved with xcalib (and easy-effects for audio).

Here is what I do in KDE:

bind Alt+PgUp to 

    xcalib -clear

bind Alt+PgDown to 

    xcalib -red 1 1 99 -green 1 1 95 -blue 1 1 90 -alter

or you might want

    xcalib -alter -contrast 60

This is very handy at night with all the lights off and on long airplane flights because it makes the screen a lot darker (with each additional key press) than it can be with the minimum display brightness setting

It looks like xcalib only works in X11, and Windows. For Wayland and Mac OS I'm sure there is something similar (beyond the built-in night modes)

I'm sure someone else can provide an ffmpeg specific solution, but I hope this helps.

However, I will note that reducing brightness intrinsically reduces dynamic range. You will need to increase contrast to compensate or something. xcalib has a weird definition of contrast, probably limited by implementation details, you can only choose from 1-100
