# Valid input.

while True:
    number=input("Enter a number:")
    number=int(number)
    if 1<=number<=10:
        print("Thanks")
        break
    else:
        print("INVALID")
