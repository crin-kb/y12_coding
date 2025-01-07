q = input("Do you want to count up or down?").lower()

if q == "up":
    start = int(input("Enter top number: "))
    for i in range(1, start + 1):
        print(i)

elif q == "down":
    start = int(input("Enter number below 20: "))
    for i in reversed(range(start , 21 )):
        print(i)
else:
    print("I don't understand.")