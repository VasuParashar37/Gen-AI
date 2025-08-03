pet = input("enter the type of pet you have ")
age = int(input("enter the age of pet: " + pet + " "))

if pet=="dog":
    if age<2:
        print("puppy food")
    else:
        print("dog food")
elif pet=="cat":
    if age<2:
        print("kitten food")
    else:
        print("adult cat food")