You might have luck with getvcp / setvcp, ie:

    sudo modprobe i2c-dev
    sudo ddcutil getvcp --mfg GSM 10

I'm not aware of a way to do that within KDE
