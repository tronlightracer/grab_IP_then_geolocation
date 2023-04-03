#!/usr/bin/bash
#NF gives the total number of fields in a string
ip_addr=$(host $1 | head -n 1 | awk '{print $NF}')
echo $ip_addr 
python3 ipinfo.py --ip $ip_addr
