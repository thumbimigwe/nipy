#!/usr/bin/python3

def isprime(number):
    if number == 1:
        print("1 is Special")
        return False
    for x in range(2, n):
        if number % x == 0:
            print("{} equals {} x {}".format(number, x, number // x))
            return False
    else:
        print(number, "is a prime number")
        return True
for n in range(1, 20):
    isprime(n)
