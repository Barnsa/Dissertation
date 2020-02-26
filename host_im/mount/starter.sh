#!/bin/bash
#bash
## Setting up everything for the output greating banner
/etc/init.d/ssh start
mkdir /tmp/stash
chmod a+rwx /tmp/stash
python3 /root/mount/ftp_av.py

## greating banner with IP and nmap for debug, start bash for control
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24)"
echo
echo "----------------"
echo "Dumb Client"
echo "----------------"
echo
echo $ip
echo "$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24 | xargs nmap)"
bash
