#!/bin/bash
#bash
/etc/init.d/ssh start
python3 /ai_server_code.py &
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24)"
echo
echo "----------------"
echo "Dumb Client"
echo "----------------"
echo
echo $ip
echo "$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -c 14-24 | xargs nmap)"

bash