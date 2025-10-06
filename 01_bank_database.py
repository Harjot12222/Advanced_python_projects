accounts = {}

def create_account():
    try:
        pin = int(input("Enter a 4-digit PIN for your account: "))
        if pin < 1000 or pin > 9999:
            print("❌ PIN must be 4 digits!")
            return
        amount = float(input("Enter the initial amount in the account: "))
        if amount < 0:
            print("❌ Amount cannot be negative!")
            return
    except ValueError:
        print("❌ Please enter valid numbers!")
        return
    name = input("Enter account holder's name: ").strip()
    accounts[name.lower()] = {"name": name, "amount": amount, "pin": pin}
    print(f"✅ Account '{name}' added successfully!\n")

def view_account():
    if not accounts:
        print("No accounts yet.\n")
        return
    name = input("Enter the name to view account: ").strip().lower()
    try:
        pin = int(input("Enter the PIN: ").strip())
    except ValueError:
        print("❌ PIN must be numeric!\n")
        return
    details = accounts.get(name)
    if details and details["pin"] == pin:
        print(f"💰 Account balance for {details['name']}: {details['amount']}\n")
    else:
        print("❌ Invalid credentials. Please try again.\n")

def deposit():
    if not accounts:
        print("No accounts yet.\n")
        return
    name = input("Enter the name to deposit into: ").strip().lower()
    try:
        pin = int(input("Enter the PIN: ").strip())
    except ValueError:
        print("❌ PIN must be numeric!\n")
        return
    details = accounts.get(name)
    if details and details["pin"] == pin:
        try:
            deposit_amount = float(input("Enter the amount to deposit: "))
            if deposit_amount <= 0:
                print("❌ Deposit amount must be positive!\n")
                return
            details["amount"] += deposit_amount
            print(f"✅ {deposit_amount} deposited. New balance: {details['amount']}\n")
        except ValueError:
            print("❌ Enter a valid number!\n")
    else:
        print("❌ Invalid credentials. Please try again.\n")

def withdraw():
    if not accounts:
        print("No accounts yet.\n")
        return
    name = input("Enter the name to withdraw from: ").strip().lower()
    try:
        pin = int(input("Enter the PIN: ").strip())
    except ValueError:
        print("❌ PIN must be numeric!\n")
        return
    details = accounts.get(name)
    if details and details["pin"] == pin:
        try:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= 0:
                print("❌ Withdraw amount must be positive!\n")
                return
            if details["amount"] < withdraw_amount:
                print("❌ Insufficient balance. Transaction aborted.\n")
                return
            details["amount"] -= withdraw_amount
            print(f"✅ {withdraw_amount} withdrawn. New balance: {details['amount']}\n")
        except ValueError:
            print("❌ Enter a valid number!\n")
    else:
        print("❌ Invalid credentials. Please try again.\n")

def main():
    while True:
        print("\n__Bank System__")
        print("1. Create new account")
        print("2. Check balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("Thanks, have a great day ❤️")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-5.\n")

if __name__ == "__main__":
    main()
