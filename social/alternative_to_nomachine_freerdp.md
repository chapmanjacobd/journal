I see NoMachine mentioned a lot on reddit, and while I have used it for years (along with X2Go), I hadn't heard of FreeRDP before. I accidentally stumbled into it via an online man page.

I was having trouble recently with NoMachine on HiDPI displays in Fedora 40. If you have the same issue, give it a go. 

The packages on Fedora are `freerdp` for the client and `freerdp-server` for the server.

I run it like this via SSH. First on the server:

    freerdp-shadow-cli -auth /ipc-socket:/run/user/1000/rdp

And then on the client:

    ssh server -L /run/user/1000/rdp:/run/user/1000/rdp 'sleep 1'
    setsid -f ssh server -L /run/user/1000/rdp:/run/user/1000/rdp 'sleep 20'
    sleep 1

    expect -c '
    set timeout -1
    spawn xfreerdp -authentication +clipboard +auto-reconnect -audio -decorations /v:/run/user/1000/rdp /network:broadband-low /smart-sizing /workarea /rfx /gfx:AVC420,thin-client,progressive,rfx /compression-level:2
    expect "Domain:"
    send "\r"
    expect "Password:"
    send "\r"
    expect eof
    '

You can use TCP too but I like file sockets. I run it without window decorations but if you want them remove `-decorations`
