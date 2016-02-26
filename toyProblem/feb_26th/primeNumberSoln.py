def prime(number):
    for i in range(2,number,1): #([start], stop[, step])
        if number % i == 0:
            return False

    return True
entry = int(input("Please enter the number: "))

while True:
    if prime(entry):
        print ("It's a prime number. ")
        break

    else:
        print ("It's not a prime number.. ")
        break