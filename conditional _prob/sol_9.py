# Pet food recommendation.

pet=input("Pet name is: ")
age=input("Pet age is:")
age=int(age)


if pet=="Dog":
    if age<2:
        food="Puppy food"
    else:
        food="whatever u like"



if pet=="Cat":
    if age>5:
        food="Senior cat food"
    else:
        food="whatever she likes"


print("Recommend food is:",food)