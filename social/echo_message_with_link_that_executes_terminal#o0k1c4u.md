You can use the commandline command to do it one time which might be close to what you want:

    commandline -r 'echo hello'

will replace the commandline with `echo hello`. It doesn't seem like much when manually running it but as part of a larger function it is quite useful:

    sshfs ...; commandline -r "fusermount -zu /net/web/"
