#/usr/bin/python
# -*- coding: utf-8 -*-

# Release vom 17.10.2019 by t.ewert@wlh.io

# Fremd Module:
import sys
sys.path.append('modules/')

from spam_lists import SPAMHAUS_DBL
import ddumpster
from shell import shell
import urllib
from geopy.geocoders import Nominatim
from crtsh import crtshAPI
import json
import warnings
warnings.filterwarnings("ignore")

# wlh Module

import whois
import reverse_whois
import reverse_ip
import dnssec
import response_time
import cn_fw
import freemail
import ip_history
import reverse_mx_lookup
import reverse_ns_lookup
import propagation

if len(sys.argv) > 1:
    choice = sys.argv[1]
else:
    print """
    
        -----------------------------------------------------------------------------------------------
                             _           _ 
                            (_)         | |
          __      _____  ___ _ _ __   __| |
          \ \ /\ / / _ \/ __| | '_ \ / _` |
           \ V  V / (_) \__ \ | | | | (_| | 
            \_/\_/ \___/|___/_|_| |_|\__,_|    version: 2.0

          whitelishackers.com by [Tom]
        ------------------------------------------------------------------------------------------------
        
        1  - DNSDumpster (3)
        2  - Whois (1)
        3  - Manufactor Network Interface (HEX format for a macaddress "00:00:00:00:00:00") (4)
        4  - Ping (4 Ping from local maschine) (1)
        5  - Testing certificates for webserver (crt.sh) (5)
        6  - Reverse Whois (2)
        7  - Reverse IP (2)
        8  - DNSSEC Test (2)
        9  - Response time from worldwide locates server to the target (2)
        10 - Header from a webserver (1)
        11 - Chinese firewall test (2)
        12 - Free Email Checkup (2)
        13 - IP history for a domain (2)
        14 - ASN search for a IP
        15 - Reverse DNS (local host call) (2)
        16 - Spam DB lookup
        17 - NsLookUp Type=any (1)
        18 - NsLookUp Type=soa|a|cname|ptr|mx (1)
        19 - Portscan with local installed "nmap" (nmap -v <IP|Domain>) - Script must be started as SUDO -
        20 - Vulnerability scan with local installed "nmap" (nmap -v -A <IP|Domain>) - Script must be started as SUDO -
        21 - Reverse NS Lookup (Nameserver is needed) (2)
        22 - Reverse MX Lookup (Mailserver is needed) (2)
        23 - Check DNS propagation (2)
        24 - Decode URL (2)
        25 - GeoIP Country (6)
        26 - GeoIP City (6)
        Exit with <ENTER>
        
        (1) using local commands like ping, host, curl, nslookup, whois
        (2) using external service from https://viewdns.info
        (3) using external service from https://dnsdumpster.com
        (4) using external service from https://api.macvendors.com
        (5) using external service from https://crt.sh
        (6) using external service fromhttps://geoip.maxmind.com
        
          """
    choice = raw_input("Enter the number of the check: ")

if choice == "1":
    param = raw_input("Enter a domain name: ")
    ddumpster.do_dump(param)

elif choice == "2":
    param = raw_input("Enter a domain name: ")
    whois.do_whois(param)
    
elif choice == "3":
    param = raw_input("Enter the macaddress: ")
    url = "https://api.macvendors.com/" + param
    erg = shell("curl -sK -X GET %s" % url)
    for i in erg.output():
        print i

elif choice == "4":
    param = raw_input("Enter a domain or ip: ")
    erg = shell("ping -c 4 %s" % param)
    for i in erg.output():
        print i

elif choice == "5":
    param = raw_input("Enter a domain name: ")
    print "\n  --  This check can last some minutes!  --  \n"
    try:
        print json.dumps(crtshAPI().search(param), indent=2)
    except:
        print " The service crt.sh is not available"
    print "Certificates download is ongoing!"
    shell("./crt.sh %s" % param)
    print "The certificate are stored as *.html files under output/crt!"

elif choice == "6":
    print " You ca enter a name (<john+doe>) or an emailaddress"
    param = raw_input("Enter your searchparameter: ")
    reverse_whois.do_reverse_whois(param)
    
elif choice == "7":
    param = raw_input("Enter a domain or an IP: ")
    reverse_ip.do_call(param)
    
elif choice == "8":
    param = raw_input("Enter a domain name: ")
    dnssec.do_call(param)
    
elif choice == "9":
    param = raw_input("Enter a domain or an IP: ")
    response_time.do_call(param)

elif choice == "10":
    param = raw_input("Enter a domain name: ")
    erg = shell("curl -I -L http://%s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "11":
    param = raw_input("Enter a domain name: ")
    cn_fw.do_call(param)
    
elif choice == "12":
    param = raw_input("Enter a domain name: ")
    freemail.do_call(param)
    
elif choice == "13":
    param = raw_input("Enter a domain name: ")
    ip_history.do_call(param)
    
elif choice == "14":
    param = raw_input("Enter an IP address: ")
    erg = shell("curl https://api.iptoasn.com/v1/as/ip/%s" % param)
    for i in erg.output():
        for j in i[1:-1].split(","):
            print j
            
elif choice == "15":
    param = raw_input("Enter an IP address: ")
    erg = shell("host %s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "16":
    param = raw_input("Enter an IP address: ")
    var = param in SPAMHAUS_DBL
    if var == True:
        print "Your IP(%s) is on a SpamDatabase" % param
    else:
        print "No SpamDB entries for your IP (%s)" % param
        
elif choice == "17":
    param = raw_input("Enter an IP address or a domain: ")
    erg = shell("nslookup -type=any %s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "18":
    param = raw_input("Enter a domain name or an IP address: ")
    typ = raw_input("Please choose typ of request (soa|a|cname|ptr|mx): ")
    erg = shell("nslookup -type=%s %s" % (typ, param))
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "19":
    param = raw_input("Enter a domain name or an IP address: ")
    try:
        print "This scan can last some minutes!"
        erg = shell("/usr/local/bin/nmap -v %s" % param)
        print "\n"
        for i in erg.output():
            print i
    except:
        print "Script mustbe started as SUDO or namp is not installed!"
        
elif choice == "20":
    param = raw_input("Enter a domain name or an IP address: ")
    try:
        print "This scan will last some minutes!"
        erg = shell("/usr/local/bin/nmap -v -A %s" % param)
        print "\n"
        for i in erg.output():
            print i
    except:
        print "Script must be started as SUDO or namp is not installed!"
        
elif choice == "21":
    try:
        param = raw_input("Enter the domain or IP address of a nameserver: ")
        reverse_ns_lookup.do_call(param)
    except:
        print "That IPaddress or domain is not a nameserver"
        
elif choice == "22":
    try:
        param = raw_input("Enter the domain of a mailservers: ")
        reverse_mx_lookup.do_call(param)
    except:
        print "That IPaddress or domain is not a Mailserver"

elif choice == "23":
    param = raw_input("Enter a domain name: ")
    propagation.do_call(param)

elif choice == "24":
    param = raw_input("Please enter a url string: ")
    print urllib.unquote_plus(param)
    
elif choice == "25":
    param = raw_input("Please enter an IP address: ")
    erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/country/%s?pretty" % param)
    for i in erg.output():
        print i
        
elif choice == "26":
    georef = []
    param = raw_input("Please enter an IP address: ")
    erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/city/%s?pretty" % param)
    for i in erg.output():
        print i
        if "latitude" in i:
            georef.append(i.lstrip()[12:-2])
        if "longitude" in i:
            georef.append(i.lstrip()[13:-2])
        
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse(georef)
    print "\n"
    print "Last known address to which IP address is assigned: "
    print "\n"
    print(location.address)
