#!/bin/bash
#bash
## Setting up everything for the output greating banner
echo
echo "----------------------------------------------------------"
echo "Dumb Client"
echo "----------------------------------------------------------"
echo
echo "----------------------------------------------------------"
echo "Running machine learning optimiser"
echo "----------------------------------------------------------"
echo
python3 /root/mount/malware-classification-master/learning.py 
/etc/init.d/ssh start
mkdir /tmp/stash
chmod a+rwx /tmp/stash
python3 /root/mount/ftp_av.py &

echo
echo "----------------------------------------------------------"
echo "Installing malware classifier dependancies"
echo "----------------------------------------------------------"
echo
# Possible fix for PE file creation using pyinstaller and wine
# Setup for malware classifier
cd /root/mount && wine msiexec /i python-2.7.9.amd64.msi /qb
wine ~/.wine/drive_c/Python27/python.exe -m pip install pyinstaller


## greating banner with IP and nmap for debug, start bash for control
#### set to cut 14-25 for 3 digit IP's
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-25)"
echo
echo "----------------------------------------------------------"
echo "Dumb Client"
echo "----------------------------------------------------------"
echo
echo $ip
echo "$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-25 | xargs nmap)"
bash
