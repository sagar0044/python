# Multiplication table printer.

number=input("enter the number:")
number=int(number)

for i in  range(1,11):
    if i==5:
        continue
    print(number,'x',i,'=', number * i)

