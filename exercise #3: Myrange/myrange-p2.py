#!/usr/bin/env python

import sys

def myrange2(x, y, z):
    for x in range(x, y, z):
        print(x)

if __name__ == "__main__":
    myrange2(int(sys.argv[1]),
             int(sys.argv[2]),
             int(sys.argv[3]))
