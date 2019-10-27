#/usr/bin/python

from shell import shell
import warnings
warnings.filterwarnings("ignore")


def do_call(param):
    
    url = "https://viewdns.info/chinesefirewall/?domain=%s" % param
    erg = shell("./curl_call.sh %s" % url)
    fh = open("tmp/erg.html", "r")
    fh_erg = open("output/ergebnis_osint.txt", "a")
    fh_erg.write(" \n----  CN FIREWALL ----\n ")
    for line in fh.readlines():
        if "the presence of GeoDNS on this domain name" in line:
            print """
            DNS servers in China returned different IP addresses to those returned by the root servers.
            This could indicate DNS poisoning by the Great Firewall of China.
            It could also just indicate the presence of GeoDNS on this domain name.
                """
            fh_erg.write("DNS servers in China returned different IP addresses to those returned by the root servers.\n") 
            fh_erg.write("This could indicate DNS poisoning by the Great Firewall of China.\n") 
            fh_erg.write("It could also just indicate the presence of GeoDNS on this domain name.\n")   
        if "All servers were able to reach your site" in line:
            print """
            All servers were able to reach your site.
            This means that your site should be accessible from within mainland China.
                """
            fh_erg.write("All servers were able to reach your site.\n")
            fh_erg.write("This means that your site should be accessible from within mainland China.\n")
    fh_erg.close()    
