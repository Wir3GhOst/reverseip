#!/usr/bin/python
# -*- coding: utf8 -*-
#Reverseip Tool
#Python 2.7
# __author__ = 'camoufl4g3'

from BeautifulSoup import BeautifulSoup
import urllib2


import sys,optparse,socket

def Main():

    parser = optparse.OptionParser("usage: %prog [options] -d domain.com")

    parser.add_option('-d',
                      action = "store",
                      dest   = "domain",
                      type   = "string",
                      help = "For scan reverseip enter domain name")


    (option,args) = parser.parse_args()


    if option.domain == None:
        print parser.usage
        sys.exit(0)

    else:

        url = "http://api.hackertarget.com/reverseiplookup/?q="+option.domain

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())

        print "\n"+"#" * 30+"\n"

        print "__author__ = 'camoufl4g3'"

        print "\n"

        for x in soup:

           print "{}".format(x)

        print "\n"+"#" * 30+"\n"


if __name__ == "__main__":
    Main()


