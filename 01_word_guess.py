import random

def word_guess_game():
    print("\n🎯 Welcome to the Sequential Word Guessing Game!")
    words = ["python", "coding", "please", "developer", "project"]
    secret_word = random.choice(words)
    word_chars = list(secret_word)
    user_progress = ["_" for _ in word_chars]
    tries = 10
    index = 0

    print("Your goal: Guess each letter in the correct order!")
    print("You have", tries, "tries.\n")

    while tries > 0 and index < len(word_chars):
        print("Current progress:", " ".join(user_progress))
        guess = input(f"Enter your guess for letter {index + 1}: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only a single alphabet letter.\n")
            continue

        if guess == word_chars[index]:
            print("✅ Correct! Moving to the next letter.\n")
            user_progress[index] = guess
            index += 1
        else:
            print("❌ Wrong letter! Starting over from the beginning.\n")
            user_progress = ["_" for _ in word_chars]
            index = 0

        tries -= 1
        print(f"Tries left: {tries}\n")

    if index == len(word_chars):
        print(f"🎉 Congratulations! You guessed the word '{secret_word}' correctly!")
    else:
        print(f"💀 Out of tries! The correct word was '{secret_word}'. Better luck next time!")

if __name__ == "__main__":
    word_guess_game()
