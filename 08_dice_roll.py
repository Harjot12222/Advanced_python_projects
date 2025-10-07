import random

def dice_game():
    history = []
    while True:
        confirm = input("Do you want to roll the dice? (y/n): ").lower().strip()
        if confirm == "y":
            dice_roll = random.randint(1, 6)
            print(f"🎲 You rolled: {dice_roll}")
            history.append(dice_roll)
        elif confirm == "n":
            if history:
                print("Your dice roll history:", history)
            else:
                print("No rolls yet.")
            print("Thanks for playing! ❤️")
            break
        else:
            print("❌ Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    dice_game()
