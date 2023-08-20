here is how I solved it but I only worry about my TV turning off.. I think it will also cover your case

    kwriteconfig5 --file powermanagementprofilesrc --group AC --group DPMSControl --key idleTime 99999
    qdbus-qt5 org.freedesktop.PowerManagement /org/kde/Solid/PowerManagement reparseConfiguration
