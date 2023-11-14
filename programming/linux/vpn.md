
wgcf register

wgcf generate

sudo cp ./wgcf-profile.conf /etc/wireguard/cloudflare.conf

Then wireguard-tools (sudo dnf install wireguard-tools) can be used to connect to the 1.1.1.1 (Cloudflare WARP) with the command:

wg-quick up cloudflare

To disconnect:

wg-quick down cloudflare
https://github.com/ViRb3/wgcf

