https://github.com/ViRb3/wgcf

wgcf register

wgcf generate

sudo cp ./wgcf-profile.conf /etc/wireguard/cloudflare.conf

sudo dnf install wireguard-tools

wg-quick up cloudflare

To disconnect:

wg-quick down cloudflare
