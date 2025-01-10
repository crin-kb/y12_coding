foods = {}
for i in range(5):
    food = input("Big Smoke: \"What is your fav foods fool?\" ")
    foods[i] = food
    print(f"Big Smoke: \"{food} has been added to the dictionary!\" ")
print(f"Big Smoke: \"These are your favourite foods fool!: {foods}\" ")
yuck = input("Big Smoke: \" Which one of these do you love the least?\" ")

if yuck in foods:
    del foods[foods.index(yuck)]
    print(f"Big Smoke: \"{yuck} has been removed from the dictionary!\" ")
    foods.sort()
    print(f"Big Smoke: \"These are your new favourite foods fool!: {foods}\" ")

