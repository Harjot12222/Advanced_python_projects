# -----------------------------------------
# 🎯 Number Guessing Game
# -----------------------------------------

import random

def play_game():
    number = random.randint(0, 100)
    print("\nWelcome to the Number Guessing Game!")
    print("Guess the number between 0 and 100.\n")

    difficulty = input("Choose difficulty level (E - Easy, M - Medium, H - Hard): ").lower()

    if difficulty == "e":
        attempts_allowed = 15
    elif difficulty == "m":
        attempts_allowed = 10
    elif difficulty == "h":
        attempts_allowed = 5
    else:
        print("❌ Invalid difficulty choice.")
        return

    print(f"You have {attempts_allowed} attempts. Good luck!\n")

    attempts = 0
    while attempts < attempts_allowed:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")

        if attempts == attempts_allowed:
            print(f"❌ Out of attempts! The correct number was {number}.")

while True:
    user_input = input("\nWould you like to play the Number Guessing Game? (y/n): ").lower()
    if user_input == "y":
        play_game()
    elif user_input == "n":
        print("👋 Thanks for playing. Have a great day ❤️")
        break
    else:
        print("⚠️ Invalid input, please type 'y' or 'n'.")
