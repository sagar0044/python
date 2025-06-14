# Factorial calculator.
number=input("Enter a number:")
number=int(number)
fact=1

while number>0:
    fact=fact*number
    number-=1
print("Factorial is: ",fact)
