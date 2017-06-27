#!/usr/bin/python

import sys, time

def countdown(num):
    print 'starting'
    while num > 0:
        print num
        yield num
        num -= 1
        time.sleep(2)

if __name__ == '__main__':
    val = countdown(int(sys.argv[1]))
    try:
        for i in val:
            next(val)
    except StopIteration:
        pass
