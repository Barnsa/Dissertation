#!/bin/bash
counter=1
while [ $counter -le 2 ]
do
    echo $counter
    python3 /root/mount/CnC_Brain.py
    ((counter++))
done
echo All done