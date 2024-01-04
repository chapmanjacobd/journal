sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
 
# Flush All Iptables Chains/Firewall rules #
sudo iptables -F
 
# Delete all Iptables Chains #
sudo iptables -X
 
# Flush all counters too #
sudo iptables -Z 
# Flush and delete all nat and  mangle #
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -t raw -F
sudo iptables -t raw -X
