# Coffee customization.

order_size=input("Desired order is :")
extra_shot=input("Yes / No :")

if extra_shot=="Yes":
    coffee=order_size + " coffee with an extra shot"
else:
    coffee=order_size + " coffee "
print(coffee)