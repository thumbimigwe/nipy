#!/usr/bin/python3

#exceptions

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)

except IOError as e:
    print("something bad happened ({})".format(e))

print("after badness")