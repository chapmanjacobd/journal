You have a few options... you could rsync the firefox profile folder. You could try X11 forwarding, xrdp, or Waypipe. Or use something like NoMachine or freerdp:

on your server

    apt install freerdp3 firefox
    freerdp-shadow-cli -auth /port:35589 /bind-address:127.0.0.1

locally

    ssh server -L 35589:localhost:35589 'sleep 20' &
    xfreerdp -authentication +auto-reconnect /gdi:sw /network:auto /v:localhost:35589 /workarea /smart-sizing /clipboard
