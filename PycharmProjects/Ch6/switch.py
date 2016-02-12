#!/usr/bin/python3

def main():
    choices = dict(
        one = "first",
        two = "second",
        three = "third"
    )
    v = 'three'
    print(choices.get(v,'other'))

if __name__ == "__main__": main()
