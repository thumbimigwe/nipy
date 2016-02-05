#!/usr/bin/python3

#exceptions

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)

except:
    print("something bad happened")

print("after badness")