I mean firewall access, public key infrastructure/management, passwordless login. 

A simple example: https://github.com/chapmanjacobd/computer/blob/main/.config/fish/functions/key-refresh-ssh.fish but if you have many machines or users you'll want a system for key management (key invalidation, expiration, rotation [when hardware changes]). Or perhaps even better, a Certificate Authority system to enforce multi-factor authentication and user management with SSH.

SSH defaults in popular distros are usually pretty secure but you might want to verify that:

    PermitRootLogin no
    PasswordAuthentication no
    PermitEmptyPasswords no
    KbdInteractiveAuthentication no

As well as make sure the version of the ssh-server is using recent key exchange scheme like X25519 / Curve25519.

With NFS I suppose you would need to solve security yourself. Perhaps you could just use a VPN and call it a day. Configuration seems non-trivial but then again, to get sshfs to do what you want you might need to fiddle with the settings as well ie. `sshfs -o noauto,noatime,_netdev,reconnect,ConnectTimeout=10,ServerAliveInterval=8,TCPKeepAlive=no`
