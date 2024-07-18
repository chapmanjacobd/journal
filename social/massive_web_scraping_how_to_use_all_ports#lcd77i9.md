I saw this a few weeks ago: https://github.com/robertdavidgraham/masscan

but I wonder if your problem is related to Nagle's algorithm. Maybe you need to use TCP_NODELAY when creating TCP sockets
