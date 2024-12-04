rain = input("Is it raining?").lower()

if rain == "yes":
    win  = input("Is it windy?").lower()
    
    if win == "yes":
        print("It's too windy for an umbrella!")
    
    else:
        print("Bring an umbrella!")
else:
    print("No need for an umbrella. Enjoy your day!")



