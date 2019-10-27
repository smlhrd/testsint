#/usr/bin/python
# -*- coding: utf-8 -*-

from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

def do_dump(domain):
    
    fh_erg = open("output/ergebnis_osint.txt", "w")
    print('Testing... : {}'.format(domain))
    fh_erg.write('Testing... : {}'.format(domain))
    fh_erg.write("\n")
    res = DNSDumpsterAPI(False).search(domain)
    print("\n---- Domain ----\n")
    fh_erg.write("---- Domain ----\n")
    print(res['domain'])
    fh_erg.write(res['domain'])
    fh_erg.write("\n")
    
    print("\n---- DNS Servers ----\n")
    fh_erg.write("\n---- DNS Servers ----\n")
    for entry in res['dns_records']['dns']:
        print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        fh_erg.write(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        fh_erg.write("\n")
    
    print("\n---- MX Records ----\n")
    fh_erg.write("\n---- MX Records ----\n")
    for entry in res['dns_records']['mx']:
        print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        fh_erg.write(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
        fh_erg.write("\n")
    
    print("\n---- Host Records (A) ----\n")
    fh_erg.write("\n---- Host Records (A) ----\n")
    for entry in res['dns_records']['host']:
        if entry['reverse_dns']:
            print(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
            fh_erg.write(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
            fh_erg.write("\n")
        else:
            print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
            fh_erg.write(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
            fh_erg.write("\n")
    
    print("\n---- TXT Records ----\n")
    fh_erg.write("\n---- TXT Records ----\n")
    for entry in res['dns_records']['txt']:
        print(entry)
        fh_erg.write(entry)
        fh_erg.write("\n")
    fh_erg.close()

    map_out = "output/" + domain + "_dnsdump.png" 
    open(map_out,'wb').write(res['image_data'].decode('base64'))
    
    xls_out = "output/" + domain + "_dnsdump.xlsx"
    open(xls_out,'wb').write(res['xls_data'].decode('base64')) # example of saving xlsx
    
    
    print "\nOutputdaten und Map wurden gespeichert in: \n\n - %s\n - %s" % (xls_out, map_out)
    print "\n"
