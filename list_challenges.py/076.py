guest = []
for i in range(4):
    ppl = input("Enter Part guest: ")
    guest.append(ppl)
    print(f"{ppl} has been added to the guest list!")

print("Do you want to add another guest? y / n")
ans = "y / n".lower()
if ans == "y" or "yes":
    while ans == "y" or "yes!":
         ppl = input("Enter Part guest: ")
         guest.append(ppl)
         print(f"{ppl} has been added to the guest list!")
         print("Do you want to add another guest? y / n")
         ans == "y / n".lower()
         if ans == "n" or "no":
            break
if ans == "n" or "no":
    print("Here are the guests:")
    for p in guest:
        print(p)




    
