#/usr/bin/python
# -*- coding: utf-8 -*-

# Release vom 07.07.2019 by t.ewert@wlh.io

# Fremd Module:
from spam_lists import SPAMHAUS_DBL
import ddumpster
from shell import shell
import urllib
from geopy.geocoders import Nominatim
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


print """
    
    1  - DNSDUMPSTER
    2  - Whois
    3  - Manufactor Network Interface
    4  - Ping (4 Ping vom lokalen Rechner)
    5  - Traceroute
    6  - Reverse Whois
    7  - Reverse IP
    8  - DNSSEC Test
    9  - Response Time vom VienDNS Server
    10 - Header und Ereichbarkeit eines Webserver abfragen
    11 - Chinese Firewall Test
    12 - Free Email Checkup
    13 - IP History fuer eine Domain
    14 - ASN suchen zu einer IP
    15 - Reverse DNS (local host call)
    16 - Spam DB lookup
    17 - NsLookUp Type=any
    18 - NsLookUp Type=soa|a|cname|ptr|mx
    19 - Portscan mit lokalem "nmap" (nmap -v <IP|Domain>)
    20 - Scan mit lokalem "nmap" (nmap -v -A <IP|Domain>)
    21 - Reverse NS Lookup
    22 - Reverse MX Lookup
    23 - Check DNS propagation
    24 - Decode URL
    25 - GeoIP Country
    26 - GeoIP City
      """  
choice = raw_input("Geben sie die Nummer ein: ")

if choice == "1":
    param = raw_input("Geben sie Domain ein: ")
    ddumpster.do_dump(param)
    
elif choice == "2":
    param = raw_input("Geben sie Domain ein: ")
    whois.do_whois(param)
    
elif choice == "3":
    param = raw_input("Geben sie die Mac Adresse ein: ")
    url = "https://api.macvendors.com/" + param
    erg = shell("curl -sK -X GET %s" % url)
    for i in erg.output():
        print i

elif choice == "4":
    param = raw_input("Geben sie das Ziel ein: ")
    erg = shell("ping -c 4 %s" % param)
    for i in erg.output():
        print i
elif choice == "5":
    param = raw_input("Geben sie das Ziel ein: ")
    print "\n  --  Achtung die Ausfuehrung eines Trace kann mehrere Minuten dauern!  --  \n"
    erg = shell("traceroute %s" % param)
    for i in erg.output():
        print i
        
elif choice == "6":
    print " Sie koennen einen Namen (<john+doe>) oder eine Emailadresse angeben"
    param = raw_input("Geben sie das Ziel ein: ")
    reverse_whois.do_reverse_whois(param)
    
elif choice == "7":
    print "Sie koennen eine IP oder einen Domain Namen angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    reverse_ip.do_call(param)
    
elif choice == "8":
    print "Sie koennen einen Domain Namen angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    dnssec.do_call(param)
    
elif choice == "9":
    print "Sie koennen eine IP oder einen Domain Namen angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    response_time.do_call(param)

elif choice == "10":
    param = raw_input("Geben sie eine Domain ein: ")
    erg = shell("curl -I -L http://%s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "11":
    print "Sie koennen einen Domain Namen angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    cn_fw.do_call(param)
    
elif choice == "12":
    print "Sie koennen einen Domain Namen angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    freemail.do_call(param)
    
elif choice == "13":
    print "Sie koennen einen Domain Namen angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    ip_history.do_call(param)
    
elif choice == "14":
    print "Sie koennen eine IP Adresse angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    erg = shell("curl https://api.iptoasn.com/v1/as/ip/%s" % param)
    for i in erg.output():
        for j in i[1:-1].split(","):
            print j
            
elif choice == "15":
    param = raw_input("Geben sie eine IP Adresse ein: ")
    erg = shell("host %s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "16":
    print "Sie koennen eine IP Adresse angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    var = param in SPAMHAUS_DBL
    if var == True:
        print "Your IP(%s) is on a SpamDatabase" % param
    else:
        print "No SpamDB Eintraege fuer ihre IP (%s)" % param
        
elif choice == "17":
    param = raw_input("Geben sie eine IP Adresse oder Domain ein: ")
    erg = shell("nslookup -type=any %s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "18":
    param = raw_input("Geben sie eine IP Adresse oder Domain ein: ")
    typ = raw_input("Geben wähle sie einen Abfragetyp aus (soa|a|cname|ptr|mx): ")
    erg = shell("nslookup -type=%s %s" % (typ, param))
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "19":
    param = raw_input("Geben sie eine IP Adresse oder Domain ein: ")
    erg = shell("/usr/local/bin/nmap -v %s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "20":
    print "Achtung!! Dieser Scan kann ein paar Minuten dauern"
    param = raw_input("Geben sie eine IP Adresse oder Domain ein: ")
    erg = shell("/usr/local/bin/nmap -v -A %s" % param)
    print "\n"
    for i in erg.output():
        print i
        
elif choice == "21":
    param = raw_input("Geben sie Domain/IP eines Nameservers ein: ")
    reverse_ns_lookup.do_call(param)
        
elif choice == "22":
    param = raw_input("Geben sie Domain eines Mailservers ein: ")
    reverse_mx_lookup.do_call(param)
    
elif choice == "23":
    param = raw_input("Geben sie eine Domain ein: ")
    propagation.do_call(param)

elif choice == "24":
    print "Diese Funktion decodiert URL Strings"
    param = raw_input("Geben sie den URL String ein: ")
    print urllib.unquote_plus(param)
    
elif choice == "25":
    print "Sie koennen eine IP Adresse angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
    erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/country/%s?pretty" % param)
    for i in erg.output():
        print i
        
elif choice == "26":
    georef = []
    print "Sie koennen eine IP Adresse angeben"
    param = raw_input("Geben Sie das Ziel ein: ")
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
    print "Letzte bekannte Adresse der die IP zugeordnet ist: "
    print "\n"
    print(location.address)
                        