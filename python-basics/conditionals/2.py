age = int(input("Enter the age "))
day = "Wed"
price =  12 if age>=18 else 8
if day=="Wed":
    price-=2

print(price)