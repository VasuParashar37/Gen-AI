password = input("Enter any pass to check the strength of it: ")

if len(password)<6:
    print(password + " is weak")
elif len(password)<=10: 
    print(password + " is of medium strength")
else :
    print(password + " is strong")