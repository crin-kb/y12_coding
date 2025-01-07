total = 0
for i in range(1, 6):
    x = int(input("Enter a number: "))
    q = input("Do you want your number to be included in the total?").lower()
    if q == "yes":
        total += x
    else:
        print("Number not included in total.")
print(f"Your total number: {total}")
