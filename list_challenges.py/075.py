dig = [345, 456, 678]
for meow in dig:
    print(meow)
x = int(input("Enter 3 digit number: "))
if x in dig:
    print(dig.index(x))
else:
    print("Not found.")

