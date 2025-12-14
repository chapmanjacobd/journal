#!/bin/sh

cat > /etc/apk/repositories << EOF
https://dl-cdn.alpinelinux.org/alpine/edge/main
https://dl-cdn.alpinelinux.org/alpine/edge/community
EOF

apk update
apk add chafa-dev go glib-static pcre2-static make
# Because I'm paranoid, remove the shared libs
# just not to tempt the linker
rm /usr/lib/libchafa.so*

cd /home/mount
make clean
STATIC_BUILD=1 make