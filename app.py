from country_list import get_countries

countries = get_countries()


print("Beginner, type 1")
print("Intermediate, type 2")
print("Hard, type 3")

difficulty = int(input("Choose a difficulty: "))

import random

selected_country = random.choice(countries)

letter_number = len(selected_country)

lives = {
    1: 10,
    2: 7,
    3: 5
}

if difficulty in lives:
    life = lives[difficulty]
    print(f"{['Beginner', 'Intermediate', 'Hard'][difficulty - 1]} difficulty was chosen, your lives: {life}")
    guessed_letters = []
    while life > 0:
        current_display = " ".join([c if c.lower() in guessed_letters else "_" for c in selected_country])
        print(current_display)

        if all(c.lower() in guessed_letters for c in selected_country):
            print(f"Congratulations, you won! The country was {selected_country}.")
            break

        guess = input("Choose a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed this letter.")
        elif guess in selected_country.lower():
            print("Correct!")
            guessed_letters.append(guess)
        else:
            life -= 1
            print(f"Incorrect! You have {life} lives left.")
            guessed_letters.append(guess)

    if life == 0:
        print(f"Game over. The country was {selected_country}.")
else:
    print("Invalid difficulty level chosen.")