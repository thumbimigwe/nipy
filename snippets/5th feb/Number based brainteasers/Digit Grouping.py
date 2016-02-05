#!/usr/bin/python3

# When displaying numbers it is good practice to group digits together and use the comma to separate groups of three digits. For instance 100000000 is easier to read when it is displayed as 100,000,000.
# Ask the user to enter any large number (e.g. at least 3 digits long). The program should display the result of formatting this number using the comma. For instance if the user enters 65738924 the program should return 65,738,924.

number = int(input("type in a six figure digit"))
grouping = ""
counter = 0

for digit in number [::-1]:
     if counter==3:
         grouping = digit + "," + grouping
         counter=0

     else:
         grouping = digit + grouping
         counter = +1

print("The inmber is "+grouping)
