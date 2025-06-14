# Movie ticket pricing.

age = input("enter the age:")
age=int(age)
day = input("Name of the day:")

price = 12 if age>=18 else 8
if day =="Wednesday":
    price = price - 2
print("Ticket price is $",price)