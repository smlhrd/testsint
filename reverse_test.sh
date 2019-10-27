#!/bin/bash

rm -f tmp/erg.html
rm  -f tmp/reverse_whois.txt

url=$1
curl -s -A 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36' -H 'Content-Type: html' -X GET "$url" > tmp/erg.html
