input_string=input("Enter a string:")


for char in input_string:
    if input_string.count(char)==1:
        print("Char is:",char)
        break

