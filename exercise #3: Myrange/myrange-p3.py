#!/usr/bin/env python

"""This function is a homegrown implementation of the range command.

Range Stop Options:
    Stop - stop of the range when starting at 0

Range Start, End, Increment Options:
    Start - beginning of the range
    End - end of the range
    Increment - option to set the increment that is returned between start and end

Format of usage: myrange-p2-expanded.py -s START -e END -i INCREMENT
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-y", help="number of yields to return", metavar='', type=int, required=True)
parser.add_argument("-s", help="stop/start of range", metavar='', type=int, required=True)
parser.add_argument("-e", help="end of range", metavar='', type=int)
parser.add_argument("-i", help="range increment", metavar='', type=int)
args = parser.parse_args()


def myrange2(x, y, z):

    if x != None and y == None and z == None:
        number = 0
        while number < x:
            print number
            number += 1
            yield

    if x != None and y != None and z == None:
        number = x
        while number < y:
            print number
            number += 1
            yield

    if x != None and y != None and z != None:
        number = x
        while number < y:
            print number
            number += z
            yield

if __name__ == "__main__":
    loop = myrange2(args.s,
             args.e,
             args.i)
    try:
        for i in range(args.y):
            next(loop)
    except StopIteration:
        pass
