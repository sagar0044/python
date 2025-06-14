# Grade calculator.
score = input("enter score:")
score=int(score)

if score>=101:
    print("Invalid")
    exit()

if score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
elif score>=60:
    print("Grade D")
else:
    print("Grade E")