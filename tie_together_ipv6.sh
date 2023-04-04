#!/usr/bin/bash
ip_addr=$(host $1 | head -n 2 | tail -n 1 | awk '{print $NF}')
echo $ip_addr

python3 ipinfo.py --ip $ip_addr