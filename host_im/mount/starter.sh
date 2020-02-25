#!/bin/bash
#bash
/etc/init.d/ssh start
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24)"
echo
echo "----------------"
echo "Dumb Client"
echo "----------------"
echo
echo $ip
echo "$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24 | xargs nmap)"
mkdir /tmp/stash
chmod a+rwx /tmp/stash
python3 /root/mount/host_manager.py
bash
