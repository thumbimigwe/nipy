#!usr/bin/python3

#siimple fibonacci series
#the sum of two elements defines the next set

a, b = 0, 1 #assigning 2 values

while b< 50: # while b< 50, we make b grow in a fibonacci series
    print(b)
    a, b = b, a + b

print("Done.")