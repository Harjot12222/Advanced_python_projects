import random
import string

def generate_password():
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    while True:
        user_choice = input("Would you like to generate a password? (y/n): ").lower().strip()
        if user_choice == "y":
            try:
                length = int(input("Enter the desired password length: "))
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
                # Generate password
                password = "".join(random.choice(pool) for _ in range(length))
                print(f"\nGenerated Password: {password}\n")
            except ValueError:
                print("Please enter a valid number for length.")
        elif user_choice == "n":
            print("Have a nice day! ✅")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    generate_password()
