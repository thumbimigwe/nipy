#!/usr/bin/python3

def isprime(number):
    if number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    else:
        return True


def primes(number = 1):
    while (True):
        if isprime(number): yield number
        number += 1

for number in primes():
    if number > 100: break
    print (number)
