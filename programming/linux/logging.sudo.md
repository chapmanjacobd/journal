Defaults iolog_dir=/var/log/sudo-io

# Members of the admin group may gain root privileges
%admin ALL=(ALL) LOG_OUTPUT:LOG_INPUT: ALL
# prevent recursive logging
%admin ALL=(ALL) NOLOG_OUTPUT:NOLOG_INPUT: /usr/bin/sudoreplay
