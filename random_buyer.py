import random

names = input("Please input the names of the people seperated by a comma and space eg: Sam, John, Alex")
names_list = names.split(", ")

random_person = random.choice(names_list)

print(f"{random_person} will pay for the meal!")