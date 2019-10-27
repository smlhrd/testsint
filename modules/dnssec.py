#/usr/bin/python
# -*- coding: utf-8 -*-

from shell import shell
from bs4 import BeautifulSoup
import sys
import warnings
warnings.filterwarnings("ignore")

def do_call(param):
    
    url = "https://viewdns.info/dnssec/?domain=%s" % param
    erg = shell("./curl_call.sh %s" % url)
    soup = BeautifulSoup(open('tmp/erg.html'), 'html.parser')
    fh = open('tmp/erg.html', 'r')
    fh_erg = open("output/ergebnis_osint.txt", "a")
    fh_erg.write(" \n----  Check DNSSEC ----\n ")
    for line in fh.readlines():
        if "DOES NOT have DNSSEC" in line:
            print "%s DOES NOT have DNSSEC! " % param
            fh_erg.write("%s DOES NOT have DNSSEC! " % param)
            fh_erg.write("\n")
            fh.close()

        else:
            if "DOES have DNSSEC" in line:
                print "%s DOES have DNSSEC !" % param
                fh_erg.write("%s DOES have DNSSEC! " % param)
                fh_erg.write("\n")
                fh.close()
    fh_erg.close()