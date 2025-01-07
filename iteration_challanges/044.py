ppl = int(input("How many people do you want to invite to your party?: "))

if ppl < 10:
    for i in range(ppl):
        p = input("Enter guest to invite: ")
        print(f"{p} has been invited.")
else: 
    print("Too many people have been invited.")