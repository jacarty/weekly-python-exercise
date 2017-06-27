#!/usr/bin/env python

"""This generator function reads text from a file and returns a defined number of grouped lines.

Options: 
    Filename - file to be opened
    Lines to group - optional to set the number of grouped lines to be returned by the function (default = 1)
    Number of yields - optional to set the number of yields the function should return (default = 1)

Format of usage: read_n.py -f FILENAME -l LINES_TO_GROUP -i NUMBER_OF_YIELDS
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="file to read", metavar='', default="1", type=str, required=True)
parser.add_argument("-l", help="number of lines to group", metavar='', default="1", type=int)
parser.add_argument("-i", help="number of yields to return", metavar='', default="1", type=int)
args = parser.parse_args()

filename = args.f
lines_to_group = args.l
number_of_yields = args.i


def read_n(textfile, lines):

    f = open(textfile)

    while True:
        file_lines = ''.join(f.readline()
                                    for x in range(lines))

        if not file_lines:
            break
        else:
            print file_lines
            yield file_lines

if __name__ == '__main__':
    generate = read_n(filename, lines_to_group)
    try:
        for i in range(number_of_yields):
            next(generate)
    except StopIteration:
        pass
