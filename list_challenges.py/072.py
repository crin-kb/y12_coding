subjects = ["english", "maths", "physics", "biology", "chemistry", "history"]

subject = input("Big Smoke: \"What subject do you hate fool?\" ")

if subject in subjects:
    subjects.remove(subject)
    for sub in subjects:
        print(sub)