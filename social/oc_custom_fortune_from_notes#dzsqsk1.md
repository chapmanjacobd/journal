**EDIT**

mmkay so it took me like an hour but I figured it out. By default URxvt in the fedora repo uses "[6x13](https://en.wikipedia.org/wiki/Fixed_\(typeface\))".

The setting looks like this: 

    URxvt*.font:6x13,\
                xft:FreeMono:pixelsize=12,\
                xft:DejaVuSansMono:pixelsize=12,\
                -*-unifont-*-*-*-*-*-*-*-*-*-*-*-*

    URxvt*.boldFont:6x13B,\
                xft:FreeMono:pixelsize=12:Bold,\
                xft:DejaVuSansMono-Bold:pixelsize=12,\
                -*-unifont-*-*-*-*-*-*-*-*-*-*-*-*

and now I have all my glyphs! :D


----

----

----

I'm not sure to be honest... I don't think I have one configured. I have this setting but I don't know if urxvt uses xterm entries:

    XTerm*faceName: Bitstream Vera Serif Mono

I really like the default font whichever it is... although I think it is missing some glyphs... :/

    xk@localhost ~> lsof -p (pgrep rxvt)
    COMMAND   PID USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME
    urxvt   28775   xk  cwd       DIR               0,50     1420    257 /home/xk
    urxvt   28775   xk  rtd       DIR               0,44      160    256 /
    urxvt   28775   xk  txt       REG               0,44  1296256 166676 /usr/bin/urxvt
    urxvt   28775   xk  mem       REG               0,42          166676 /usr/bin/urxvt (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           57677 /usr/share/fonts/dejavu/DejaVuSans-Bold.ttf (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           57686 /usr/share/fonts/dejavu/DejaVuSansMono-Bold.ttf (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           57689 /usr/share/fonts/dejavu/DejaVuSansMono.ttf (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           58008 /usr/share/fonts/vlgothic/VL-Gothic-Regular.ttf (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           57681 /usr/share/fonts/dejavu/DejaVuSans.ttf (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           57693 /usr/share/fonts/dejavu/DejaVuSerif.ttf (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42           28413 /usr/lib64/libfreetype.so.6.14.0 (path dev=0,44)
    urxvt   28775   xk  mem       REG               0,42          247509 /usr/lib64/libfontconfig.so.1.11.1 (path dev=0,44)
    ...
