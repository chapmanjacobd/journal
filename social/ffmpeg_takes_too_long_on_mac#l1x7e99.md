> i have no way to check if it is working or not

Try adding `-nostdin` as a global option (right next to `ffmpeg -y`). If ffmpeg is waiting for input because stdin is not a terminal that will cause it to hang without any output.

You could also try increasing verbosity. 

I also recommend running the command in an interactive shell for faster troubleshooting feedback loop before trying to wrangle it as a subprocess in python. 

Also, take a closer look at the documentation here:

- https://ffmpeg.org/ffmpeg-devices.html#Examples

- http://trac.ffmpeg.org/wiki/Capture/Desktop#macOS

Finally, as a last resort, you could try running your program with strace to see what it is doing in terms of system calls
