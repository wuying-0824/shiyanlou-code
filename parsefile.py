import os
import sys

def parse_file(path):
    f = open(path)
    i = 0
    tabs = 0
    spaces = 0
    for i, line in enumerate(f):
        spaces += line.count(' ')
        tabs += line.count('\t')
    f.close()
    return i+1, tabs, spaces

def main(path):
    if os.path.exists(path):
        lines, tabs, spaces = parse_file(path)
        print("Lines {}.   tabs {}.   Spaces {}".format(lines, tabs, spaces))
        return True
    else:
        return False

main(sys.argv[1])
