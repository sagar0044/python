# Prime number checker.

number=43


is_prime = True

if number>1:
    for i in range(2,number):
        if (number % i)==0:
            is_prime = False
            break
print(is_prime)