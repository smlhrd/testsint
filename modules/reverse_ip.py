#/usr/bin/python
# -*- coding: utf-8 -*-

from shell import shell
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")

def do_call(param):
    
    url = "https://viewdns.info/reverseip/?host=%s&t=1" % param
    erg = shell("./curl_call.sh %s" % url)
    soup = BeautifulSoup(open('tmp/erg.html'), 'html.parser')

    dom_table = soup.find_all('table')
    dom_table = dom_table[3]

    with open('tmp/reverse_whois.txt', 'w') as r:

        for rows in dom_table.find_all('tr'):
            for cells in rows.find_all('td'):
                r.write(cells.text.ljust(30))
            r.write('\n')
    fh_out = open('tmp/reverse_whois.txt', 'r')
    fh_erg = open("output/ergebnis_osint.txt", "a")
    fh_erg.write(" \n----  REVERSE IP ----\n ")
    fh_erg.write("\n")
    for line in fh_out:
        print line.rstrip()
        
        fh_erg.write(line.rstrip())
        fh_erg.write("\n")
    fh_erg.close()