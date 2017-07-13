#!/usr/bin/env python

"""For each line of the log file create a dictionary and, in turn add that to a list."""

import sys
import re

listofdict = []

ip = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
time = re.compile('\d{1,2}/\w{3}/\S+ [+]\d{4}')
web_request = re.compile('GET /(\S+)? \w{4}/\d.\d')


def logtodict(textfile):

    for each_line in open(textfile):

        dic = {
            'ip_address': ip.search(each_line).group(),
            'timestamp': time.search(each_line).group(),
            'request': web_request.search(each_line).group()
        }

        listofdict.append(dic)

    print listofdict

if __name__ == '__main__':
    logtodict(sys.argv[1])
