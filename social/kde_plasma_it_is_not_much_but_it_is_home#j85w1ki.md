Details

+ **Wallpaper**: [Magellanic Clouds over Chile by Felipe Mac Auliffe López](https://apod.nasa.gov/apod/image/2302/magellanic.jpg)
+ **process snapshot**: ps -o etime,stat,command ww
+ **bandwidth usage**: sudo iftop -n -b -P -t -o 40s -L 4
+ **device IO stats**: iostat -xh 4

I only use one monitor and one window at a time and (I alt-tab often). `krohnkite` helps with the wide aspect monitor that I use when sitting down.

I switch screens frequently throughout the day. kscreen-doctor helps with this:

    function tv
        if grep -qEi "(DisplayPort-0)" (kscreen-doctor -o | psub)
            kscreen-doctor output.HDMI-A-0.disable output.DisplayPort-0.disable output.DVI-D-0.disable
            kscreen-doctor output.HDMI-A-0.enable output.HDMI-A-0.mode.1920x1080@60
        else
            kscreen-doctor output.HDMI-1.disable output.DP-1.disable output.DVI-D-0.disable
            kscreen-doctor output.HDMI-1.enable output.HDMI-1.mode.1920x1080@60
        end
        krohnkite_off
        keepscreenon && xset s off
        pactl set-default-sink alsa_output.pci-0000_01_00.1.hdmi-stereo-extra3
    end

    function keepscreenon
        kwriteconfig5 --file powermanagementprofilesrc --group AC --group DPMSControl --key idleTime 99999
        qdbus-qt5 org.freedesktop.PowerManagement /org/kde/Solid/PowerManagement reparseConfiguration
    end

    function krohnkite_on
        kwriteconfig5 --file kwinrc --group Plugins --key krohnkiteEnabled true
        qdbus-qt5 org.kde.KWin /KWin reconfigure
    end

    function sitdown
        if grep -qEi "(DisplayPort-0)" (kscreen-doctor -o | psub)
            kscreen-doctor output.HDMI-A-0.disable output.DisplayPort-0.disable output.DVI-D-0.disable
            kscreen-doctor output.DisplayPort-0.enable
        end
        if grep -qEi "(DP-1)" (kscreen-doctor -o | psub)
            kscreen-doctor output.HDMI-1.disable output.DP-1.disable output.DVI-D-0.disable
            kscreen-doctor output.DP-1.enable
        end
        krohnkite_on
        bash -c 'kquitapp5 plasmashell || killall plasmashell; kstart5 plasmashell'
        kwin_x11 --replace & disown
        pactl set-default-sink alsa_output.pci-0000_00_1f.3.pro-output-0
    end
