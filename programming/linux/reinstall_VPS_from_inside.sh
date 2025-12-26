# should works on any cloud-init enabled hypervisor (openstack.. )

# start from a ubuntu minimal install
# we need to shrink down the used space to move it in a tmpfs of 700MB

# make sure we are on the highest kernel, so we can delete all the others ...
sudo apt update && sudo apt upgrade -y && reboot

# ... reconnect
sudo apt install lsof
sudo snap remove --purge  oracle-cloud-agent && sudo snap remove --purge core18 && sudo snap remove --purge snapd && sudo sudo apt -y purge snapd && sudo rm -rf ~/snap /snap /var/cache/snapd
sudo apt purge $(dpkg-query -Wf '${Package}\n' | grep header)  $(apt list --installed | grep -oP "^linux.*\d\d\d\d-oracle" | grep -v "$(uname -r)") linux-modules-extra-$(uname -r) lxc* lxd* vim* && sudo apt -y autoremove && sudo apt -y autoclean && sudo apt -y clean  
sudo rm -rf /var/log/* /var/lib/apt/lists/*


# ok, the disk usage of / should be less than 600MB now

cd /
mount -t tmpfs -o size=700m tmpfs mnt
tar --one-file-system -c . | tar -C /mnt -x
mount --make-private -o remount,rw /
mount --move dev mnt/dev
mount --move proc mnt/proc
mount --move run mnt/run
mount --move sys mnt/sys
sed -i '/^[^#]/d;' mnt/etc/fstab
echo 'tmpfs / tmpfs defaults 0 0' >> mnt/etc/fstab
cd mnt
mkdir old_root
mount --make-private /
unshare -m
pivot_root . old_root

# now the root storage is the RAM 

# lets restart all runnig process

service ssh restart 

# now switch to a new ssh connexion to let the old sshd terminate
 
service systemd-udevd restart
service systemd-journald restart
service systemd-networkd restart
service systemd-timesyncd restart
service systemd-resolved restart
service systemd-logind restart
service networkd-dispatcher restart
pkill agetty
pkill dbus-daemon
pkill atd
pkill iscsid
pkill rpcbind
pkill unattended-upgrades
kill 1 

# check with "lsof /old_root" that there is no remaining process 

umount -l /dev/sda1

# check :

df -h 
lsblk 

# the disk should be unmount 
# now, just copy the debian cloud image on the disk.

# curl https://cdimage.debian.org/cdimage/openstack/current/debian-10-openstack-amd64.raw | dd of=/dev/sda bs=1M

# update : 
curl -L  https://cdimage.debian.org/cdimage/openstack/testing/debian-testing-openstack-amd64.raw | dd of=/dev/sda bs=1M

sync

reboot


