#!/usr/bin/env python

import sys
import re
import operator


class LogDicts:
    """Various functions that return or sort items form a log file"""

    def __init__(self, textfile):
        self._logfile = textfile

    def logtodict(self):

        listofdict = []

        ip = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
        time = re.compile('\d{1,2}/\w{3}/\S+ [+]\d{4}')
        web_request = re.compile('GET /(\S+)? \w{4}/\d.\d')

        for each_line in open(self._logfile):

            dic = {
                'ip_address': ip.search(each_line).group(),
                'timestamp': time.search(each_line).group(),
                'request': web_request.search(each_line).group()
            }

            listofdict.append(dic)

        return listofdict

    def iterlogtodict(self):

        return (item for item in self.logtodict())

    def earliest(self, key=None):

        if key:
            return min(self.logtodict(), key=key)
        else:
            return self.logtodict()

    def latest(self, key=None):

        if key:
            return max(self.logtodict(), key=key)
        else:
            return self.logtodict()

if __name__ == '__main__':
    ld = LogDicts(sys.argv[1])
    #print ld.logtodict()
    #print ld.iterlogtodict()
    #print ld.earliest(key=operator.itemgetter('ip_address'))
    #print ld.latest(key=operator.itemgetter('ip_address'))
