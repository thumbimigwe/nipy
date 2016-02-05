#!/usr/bin/python3

# Write a program that prompts the user to enter a number and returns whether this number is an odd number or an even number.

number = int(input("Input a number to see whether its odd or even"))
if(number%2)==0:
    print(number+"This number is even")
else:
    print(number+" is an odd number")
