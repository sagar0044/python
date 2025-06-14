# Password strength checker.

char_no=input("Password is: ")


if len(char_no)<6:
    password="Weak"
elif len(char_no)<=10:
    password="Medium"
else:
    password="Strong"

print("Your password is: ",password)
