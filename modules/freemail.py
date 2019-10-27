#/usr/bin/python

from shell import shell
import warnings
warnings.filterwarnings("ignore")


def do_call(param):
    
    url = "https://viewdns.info/freeemail/?domain=%s" % param
    erg = shell("./curl_call.sh %s" % url)
    fh = open("tmp/erg.html", "r")
    fh_erg = open("output/ergebnis_osint.txt", "a")
    fh_erg.write(" \n----  FREEMAIL SERVER CHECK ----\n ")
    fh_erg.write("\n")
    for line in fh.readlines():
        if "domain DOES NOT appear" in line:
            print "This domain DOES NOT appear to provide free email addresses"
            fh_erg.write("This domain DOES NOT appear to provide free email addresses")
            fh_erg.write("\n")
        if "domain DOES appear" in line:
            print "This domain DOES appear to provide free email addresses."
            fh_erg.write("This domain DOES appear to provide free email addresses.")
            fh_erg.write("\n")
    fh_erg.close()