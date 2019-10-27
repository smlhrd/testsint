Readme zum Tool "osint_wlh.txt"

Fuer letzte Aenderungen und known_issues bitte die Datei release_notes.txt lesen.


Das Tool vereint viele Möglichkeiten der OpenSource Intelligence in einem Tool.
Geschrieben wurde das Tool in Python und nutzt sowohl Programme die lokal installiert sind,
wie z.B. ping, traceroute, curl ... , aber auch externe Quellen wie www.viewdns.info.
Bei der Abfrage von externen Quellen wird ein Curl Call abgesetzt. Dieser greift die Daten
von einer API ab, oder das Tool macht "web scraping" mit beautifulsoup4

1. Systemvorraussetzungen:
 
 ==> MacOS oder Linux (Windows wegen fehlender Tools aus der Shell nur bedingt geeignet)
 ==> Python 2.7.x
 ==> Nmap (https://nmap.org/download)
 
 In Python integrierte Module:
 
 ==> urllib (Decoder wird genutzt)
 
 Folgende externe Python Module:
 
 ==> shell (https://pypi.org/project/shell/)
 ==> dnsdumpster (https://github.com/PaulSec/API-dnsdumpster.com)
 ==> spam-list (https://pypi.org/project/spam-lists/)
 ==> beautifulsoup4 (https://pypi.org/project/beautifulsoup4/)
 ==> geopy (https://geopy.readthedocs.io/en/latest/)
 
 Folgende eigene Python Module:
 
 ==> asn_tool
 ==> clean_html
 ==> cn_fw
 ==> ddumpster
 ==> dnssec
 ==> freemail
 ==> ip_history
 ==> response_time
 ==> reverse_ip
 ==> reverse_whois
 ==> spam_db_lookup
 ==> whois
 ==> reverse_mx_lookup
 ==> reverse_ns_lookup
 
2. Installation
 
 Das Packet "osint_wlh.zip" enpacken. Es enthält das Script
 osint_wlh.py und alle eigenen Module.
 
3. Start des Tools:
 
 auf der Shell folgenden Befehl ausführen:
 	<python osint_wlh.py>
 	
 Es erscheint dann ein Auswahlmenü:
 
 	1  - DNSDUMPSTER
    2  - Whois
    3  - Manufactor Network Interface
    4  - Ping (4 Pingsaus vom lokalen Rechner)
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
    
Am Prompt die Nummer der gewünschten Funktion angeben. Danach erscheint der nächste Prompt zur Eingabe der
benötigten Daten. Hier wird auch angezeigt, welche Daten die Funktion erwartet und in welchen Format.

4. Informationen der einzelnen Funktionen

	1  - DNSDUMPSTER
		- Liefert alle DNS Informationen die über die Webseite https://dnsdumpster.com zur Verfügung stehen
		- Ergebnisse werden auch als .xls und .png Datei lokal gespeichert
    2  - Whois
    	- Whois Abfrage mit Domain und IP. Genutzt wird das lokale Tool "whois"
    3  - Manufactor Network Interface
    	- Liefert den Hersteller eines Netzwerkinterface auf Basis der MAC Adresse aus der Datenbank https://api.macvendors.com/
    4  - Ping (4 Pingsaus vom lokalen Rechner)
    	- Setzt einen Ping mit 4 Wiederholungen gegen das gewählte Ziel ab. Lokales "ping" Tool wird genutzt
    5  - Traceroute
    	- Traceroute auf ein gewähltes Ziel. Lokales Tool "traceroute" wird genutzt
    6  - Reverse Whois
    	- Eine reverse whois Abfrage gegen einen Domain Besitzer Namen oder eine Mailadresse mit Hilfe von https://viewdns.info/reversewhois/
    7  - Reverse IP
    	- Zeigt alle Doamains die auf diesem Server gehostet werden via https://viewdns.info/reverseip/
    8  - DNSSEC Test
    	- Prüft ob für eine Domain DNSSEC aktiviert ist via https://viewdns.info/dnssec/
    9  - Response Time vom VienDNS Server
    	- Responsetime eines Webservers von https://viewdns.info/ping/
    10 - Header und Ereichbarkeit eines Webserver abfragen
    	- Abfrage alle Header eines Webservers mit einem lokalen "curl" call. Hier kann dann auch der Status der Webseite erfragt werden 
    11 - Chinese Firewall Test
    	- Test ob die "Great Chinese Firewall" eine Domain/IP blockt via https://viewdns.info/chinesefirewall/
    12 - Free Email Checkup
    	- Prüft ob ein Server einen FreeMail Dienst anbietet via https://viewdns.info/freeemail/
    13 - IP History fuer eine Domain
    	- Liefert alle IP Adressen unter denen eine Domain erreichbar war via https://viewdns.info/iphistory/
    14 - ASN suchen zu einer IP
    	- Liefert die ASN zu einer IP Adresse via https://viewdns.info/asnlookup/
    15 - Reverse DNS (local host call)
    	- Nutzt das lokale "host" command um eine Reverse DNS Abfrage zu machen
    16 - Spam DB lookup
    	- Prüft ob eine Domain in einer Spamdatenbank gelistet ist (SURBL, Spamhaus ZEN and Spamhaus DBL)
    17 - NsLookUp Type=any
		- Lokal Tool "nslookup" mit dem Parameter type=any
    18 - NsLookUp Type=soa|a|cname|ptr|mx
    	- Lokal Tool "nslookup" mit Parameterauswahl (soa|a|cname|ptr|mx)
    19 - Portscan mit lokalem "nmap" (nmap -v <IP|Domain>)
    	- Standard Portscan gegen das Ziel
    20 - Scan mit lokalem "nmap" (nmap -v -A <IP|Domain>)
    	- Scan mit OS and Versions Erkennung, script scanning, and traceroute
    21 - Reverse NS Lookup
    	- Zeigt Domains an die diesen Nameserver nutzen via https://viewdns.info/reversens/
    22 - Reverse MX Lookup
    	- Zeigt Domains an die diesen Mailserver nutzen via https://viewdns.info/reversemx/
    23 - Check DNS propagation
    	- Prüft Weltweit ob Änderungen am DNS propagiert wurden via https://viewdns.info/propagation
    24 - Decode URL
    	- Decodiert URL Strings. Hier wird der decoder aus dem internen Modul "urllib" genutzt
    25 - GeoIP Country
    	- Ermittelt das Land zu einer IP Adresse mit der API von MAXMIND. Genutzt wird ein Curl Call. Achtung Lizenz erforderlich!!
    26 - GeoIP City
        - Ermittelt die Stadt zu einer IP Adresse mit der API von MAXMIND. Genutzt wird ein Curl Call. Achtung Lizenz erforderlich!!
        - Ermittelt zusätzlich die die letzte bekannte Adresse zu einer IP Adresse mit dem Modul geopy
 
 3 Erweiterung um das Script osint_wlh_all.txt
 
 In diesem Script werden alle Einzeltests zu einem Gesamttest zusammengeführt.
 Nicht getestet wird der Hersteller der Netzwerkkarten.
 Es müssen keine weiteren Module installiert werden. Das Script nutzt die selben Module wie osint_wlh.py.
 
 * Aufruf des Scripts_
 
 - python ./osint_wlh_all.py
 
 * Doing
 
 Zur Eingabe ist nur eine Domain nötig. Wenn man noch einen Namen oder eine Mailadresse zur Hand hat, dann kann auch der
 Test "reverse_whois" ausgeführt werden.
 Die restlichen benötigten Daten wie
 - IPAdresse
 - Mailserver
 - Nameserver
 
 ermittelt das Script selber.
 Sollte man nach dem Start des Scripts keine Domain eingeben, beendet sich das Script mit dem Hinweis auf die fehlenden Daten.
 Im Laufe der Abarbeitung erfragt das Script nochmals zwei Werte:
 
 - Eine URL zur Decodierung
 - Einen Parameter für einen NSLOOKUP Test
 
 Beide Parameter können leer bleiben. Bei der URL zeigt das Script dann eben nichts weiter an und bei NSLOOKUP wird eine Standardabfrage
 im Stil von "nslookup <domain> durchgeführt".
 
 Die gesammelten Ergebnisse werden in der Datei
 "<domain>_osint_erg.txt"
 im Arbeitsverzeichnis abgelegt.
 
 