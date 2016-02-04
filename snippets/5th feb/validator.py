#!/usr/bin/python3

def inputNumber(message):
     while True:
         try:
             userInput = int(input(message))
         except ValueError:
             print("not a numper. Try again.")
             continue
         else:
             return userInput
         break

username = input("What is your name?   ")
age = int(input("how old are you?   "))
