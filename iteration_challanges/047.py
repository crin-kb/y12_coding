x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
 
z = x + y 
q = input("Do you want to add another number?")

while q.lower() == "y":
    t = int(input("Enter another number: "))
    z += t
    q = input("Do you want to add another number?")

print("The sum is:", z)