#/usr/bin/python
# -*- coding: utf-8 -*-

# Release vom 31.07.2019 by t.ewert@wlh.io

# Fremd Module:
import socket
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
import sys



domain = raw_input("Geben sie die Zieldomain ein: ")

if domain == "":
    
    print "Sie muessen eine Domain eingeben. Bitte das Script neu starten und die Domain eingeben!"
    sys.exit()

# IP Adresse fuer die Domain bestimmen
    
ip_addr = socket.gethostbyname(domain)
    
print "Sie koennen einen Namen (<john+doe>) oder eine Emailadresse angeben"
print "Sie koennen die Eingabe leer lassen. Reverse_Whois wird dann nicht ausgefuehrt"
name_mail = raw_input("Geben sie das Ziel ein: ")

# Mailserver und Nameserver fuer die Domain finden

clear_list_mx = []
clear_list_ns = []
erg = shell("nslookup -type=mx %s" % domain)
for i in erg.output():
    if "mail" in i:
        x = i.split(" ")
        clear_list_mx.append(x[4][:-1])

erg = shell("nslookup -type=ns %s" % domain)
for i in erg.output():
    if "nameserver" in i:
        y = i.split(" = ")
        clear_list_ns.append(y[1][:-1])       

#####################################################    

print "\n"
print " ----  DNS DUMPSTER ---- "
print "\n"
ddumpster.do_dump(domain)
print "\n"
print " ----  WHOIS ---- "
print "\n"

whois.do_whois(domain)

print "\n"
print " ----  PING ---- "

print "\n"
fh_erg = open("ergebnis_osint.txt", "a")
fh_erg.write("\n ----  PING ---- \n")

erg = shell("ping -c 4 %s" % domain)
for i in erg.output():
    print i
    fh_erg.write(i)
    fh_erg.write("\n")
    
print "\n"
print " ----  TraceRoute ---- "
fh_erg.write("\n ----  TraceRoute ---- \n")
print "\n"
print "\n  --  Achtung die Ausfuehrung eines Trace kann mehrere Minuten dauern!  --  \n"
erg = shell("traceroute %s" % domain)
for i in erg.output():
    print i
    
    fh_erg.write(i)
    fh_erg.write("\n")
fh_erg.close()

print "\n"
print " ----  REVERSE WHOIS ---- "
print "\n"
try:
    reverse_whois.do_reverse_whois(name_mail)
except:
    fh_erg = open("ergebnis_osint.txt", "a")
    fh_erg.write("\n ---- REVERSE WHOIS ---- \n")
    fh_erg.write("\n Keine Daten zur Verarbeitung eingegeben!!\n")
    print "\n Keine Daten zur Verarbeitung eingegeben!!\n"

print "\n"
print " ----  REVERSE IP ---- "
print "\n"
    
reverse_ip.do_call(domain)

print "\n"
print " ----  CHECK DNSSEC ---- "
print "\n"
    
dnssec.do_call(domain)

print "\n"
print " ----  RESPONSE TIME ---- "
print "\n"
    
    
response_time.do_call(domain)

print "\n"
print " ----  GET HTTP HEADER ---- "
print "\n"
fh_erg = open("ergebnis_osint.txt", "a")
fh_erg.write(" \n----  REVERSE IP ----\n ")

erg = shell("curl -I -L http://%s" % domain)
print "\n"
for i in erg.output():
    print i
    fh_erg.write(i.rstrip())
    fh_erg.write("\n")
fh_erg.close()   
 
print "\n"
print " ----  CN FIREWALL ---- "
print "\n"
    
    
cn_fw.do_call(domain)
  
print "\n"
print " ----  FREEMAIL ---- "
print "\n"
       

freemail.do_call(domain)

print "\n"
print " ----  IP HISTORY ---- "
print "\n"
    

ip_history.do_call(domain)

print "\n"
print " ----  NS LOOKUP (TYPE ANY) ---- "
print "\n"
    
fh_erg = open("ergebnis_osint.txt", "a")
fh_erg.write(" \n----  NS LOOKUP (TYPE ANY) ----\n ")
fh_erg.write("\n")        
erg = shell("nslookup -type=any %s" % domain)
print "\n"
for i in erg.output():
    print i
    fh_erg.write(i.rstrip())
    fh_erg.write("\n")
    
   
print "\n"
print " ----  NS LOOKUP (FREE TYPE) ---- "
print "\n"
    
fh_erg.write(" \n----  NS LOOKUP (FREE TYPE) ----\n ")
fh_erg.write("\n")     
typ = raw_input("Geben wähle sie einen Abfragetyp aus (soa|a|cname|ptr|mx): ")
erg = shell("nslookup -type=%s %s" % (typ, domain))
print "\n"
for i in erg.output():
    print i
    fh_erg.write(i.rstrip())
    fh_erg.write("\n")
fh_erg.close()

print "\n"
print " ----  Reverse NSLOOKUP ---- "
print "\n"

for i in clear_list_ns:
    try:
        reverse_ns_lookup.do_call(i)
    except:
        fh_erg = open("ergebnis_osint.txt", "a")
        fh_erg.write(" \n----  Reverse NSLOOKUP ----\n ")
        fh_erg.write("\n") 
        print "NSLOOKUP mit Nameserver: %s liefert Fehler zurück" % i
        fh_erg.write("NSLOOKUP mit Nameserver: %s liefert Fehler zurück" % i)
        fh_erg.write("\n")
        fh_erg.close()
 
print "\n"
print " ----  REVERSE MX ---- "
print "\n"

for i in clear_list_mx:
    try:
        reverse_mx_lookup.do_call(i)
    except:
        print "Reverse MX mit Mailserver: %s liefert Fehler zurück" % i
        fh_erg = open("ergebnis_osint.txt", "a")
        fh_erg.write(" \n----  Reverse NSLOOKUP ----\n ")
        fh_erg.write("\n")
        fh_erg.write("Reverse MX mit Mailserver: %s liefert Fehler zurück" % i)
        fh_erg.write("\n")
        fh_erg.close()
        
     
print "\n"
print " ----  DECODE URL STRINGS ---- "
print "\n"
fh_erg = open("ergebnis_osint.txt", "a")
fh_erg.write(" \n----  DECODE URL STRINGS ----\n ")
fh_erg.write("\n")     
    
print "Diese Funktion decodiert URL Strings. Kann leer bleiben!"
param = raw_input("Geben sie den URL String ein: ")
print urllib.unquote_plus(param)
fh_erg.write(urllib.unquote_plus(param))
fh_erg.write("\n")
fh_erg.close()

print "\n"
print " ----  DNS PROPAGATION ---- "
print "\n"
    
propagation.do_call(domain)

print "\n"
print " ----  IP2ASN ---- "
print "\n"

fh_erg = open("ergebnis_osint.txt", "a")
fh_erg.write(" \n----  DECODE URL STRINGS ----\n ")
fh_erg.write("\n")    
erg = shell("curl https://api.iptoasn.com/v1/as/ip/%s" % param)
for i in erg.output():
    for j in i[1:-1].split(","):
        print j
        fh_erg.write(j)
        fh_erg.write("\n")
       
print "\n"
print " ----  IP2HOST ---- "
print "\n"        
fh_erg.write(" \n----  IP2HOST ----\n ")
fh_erg.write("\n") 
erg = shell("host %s" % ip_addr)
print "\n"
for i in erg.output():
    print i
    fh_erg.write(i)
    fh_erg.write("\n")
    
print "\n"
print " ----  SPAMCHECK ---- "
print "\n"
fh_erg.write(" \n----  SPAMCHECK ----\n ")
fh_erg.write("\n")
var = ip_addr in SPAMHAUS_DBL
if var == True:
    print "Your IP(%s) is on a SpamDatabase" % ip_addr
    fh_erg.write("Your IP(%s) is on a SpamDatabase" % ip_addr)
    fh_erg.write("\n")
else:
    print "No SpamDB Eintraege fuer ihre IP (%s)" % ip_addr 
    fh_erg.write("No SpamDB Eintraege fuer ihre IP (%s)" % ip_addr)
    fh_erg.write("\n")


print "\n"
print " ----  PORTSCAN ---- "
print "\n"
fh_erg.write(" \n----  PORTSCAN ----\n ")
fh_erg.write("\n")
erg = shell("/usr/local/bin/nmap -v %s" % ip_addr)
print "\n"
for i in erg.output():
    print i
    fh_erg.write(i)
    fh_erg.write("\n")
    
print "\n"
print " ----  NMAP SCAN MIT SERVICE ---- "
print "\n"
fh_erg.write(" \n----  NMAP SCAN MIT SERVICE ----\n ")
fh_erg.write("\n")
print "Achtung!! Dieser Scan kann ein paar Minuten dauern"
erg = shell("/usr/local/bin/nmap -v -A %s" % ip_addr)
print "\n"
for i in erg.output():
    print i
    fh_erg.write(i)
    fh_erg.write("\n")
 
print "\n"

print " ----  GeoIP Country ---- "
print "\n"
fh_erg.write(" \n----  GeoIP Country ----\n ")
fh_erg.write("\n")
erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/country/%s?pretty" % ip_addr)
for i in erg.output():
    print i
    fh_erg.write(i)
    fh_erg.write("\n")


print "\n"
print " ----  GeoIP City ---- "
print "\n"
fh_erg.write(" \n----  GeoIP City ----\n ")
fh_erg.write("\n")

georef = []
erg = shell("curl -u \"141447:Udkm6zdeXYgJ\" -X GET https://geoip.maxmind.com/geoip/v2.1/city/%s?pretty" % ip_addr)
for i in erg.output():
    print i
    fh_erg.write(i)
    fh_erg.write("\n")
    if "latitude" in i:
        georef.append(i.lstrip()[12:-2])
    if "longitude" in i:
        georef.append(i.lstrip()[13:-2])
        
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.reverse(georef)
print "\n"
print "Letzte bekannte Adresse der die IP zugeordnet ist: "
fh_erg.write("Letzte bekannte Adresse der die IP zugeordnet ist: ")
fh_erg.write("\n")
print "\n"
print(location.address)
fh_erg.write(location.address)
fh_erg.write("\n")
fh_erg.write(" ------  END OF FILE ------  ")
fh_erg.write("\n")
fh_erg.close()

erg = shell("mv ergebnis_osint.txt %s_osint_erg.txt" % domain)