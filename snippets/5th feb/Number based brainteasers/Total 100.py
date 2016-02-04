#!/usr/bin/python3

# Write a program that prompts the user to enter a number between 0 and 100. The program should return the number that needs to be added to reach 100. For instance if the user enters 36, the program should return 64 because 36 + 64 = 100.

number = int(input("type a number between 0 to 100...  "))
total100 = 100 - number
print("The total 100 number is..."+str(total100))
