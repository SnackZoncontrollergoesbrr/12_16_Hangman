from country_list import get_countries

countries = get_countries()


print("Beginner, type 1")
print("Intermediate, type 2")
print("Hard, type 3")

difficulty = int(input("Choose a difficulty: "))

import random

selected_country = random.choice(countries)
print(selected_country)

letter_number = len(selected_country)

print(replace()(letter_number * "_ "))

if difficulty == 1:
    life = 10
    print(f"Beginner difficulty was chosen, your lives: {life}")
    guess = input("Choose a letter: ")

elif difficulty == 2:
    life_2 = 7
    print(f"Intermediate difficulty was chosen, your lives: {life_2}")

elif difficulty == 3:
    life_3 = 5
    print(f"Hard difficulty was chosen, your lives: {life_3}")
else:
    print("Wrong number")


# print(countries[0])
# for char in countries[0]:
#     print(char)
#     if char == guess:
#         print("Nice one!")
#     else:
#         print("Try again")