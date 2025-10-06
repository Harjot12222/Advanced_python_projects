# ---------------------------------------
# 💰 Expense & Data Analysis Tool
# ---------------------------------------

from collections import Counter
import numpy as np

# --- Sample Expense Dataset ---
expenses = [
    {"amount": 200, "category": "Food", "note": "Lunch"},
    {"amount": 150, "category": "Transport", "note": "Taxi"},
    {"amount": 300, "category": "Food", "note": "Dinner"},
    {"amount": 100, "category": "Entertainment", "note": "Movie"},
    {"amount": 250, "category": "Transport", "note": "Train tickets"}
]

# --- Expense Summary ---
totals = {}
for exp in expenses:
    cat = exp["category"]
    totals[cat] = totals.get(cat, 0) + exp["amount"]

print("\n--- Expense Summary by Category ---")
for cat, total in totals.items():
    print(f"{cat}: ₹{total}")

print("\n--- Expense Bar Chart ---")
for cat, amount in totals.items():
    print(f"{cat}: {'⬜' * (amount // 50)}")

# --- User Data Collection for Statistical Analysis ---
numbers = []

while True:
    user_choice = input("\nWould you like to enter numbers for analysis? (y/n): ").lower()
    if user_choice == "y":
        try:
            num = float(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("❌ Please enter a valid number.")
    elif user_choice == "n":
        if not numbers:
            print("No numbers entered. Exiting.")
        else:
            print("✅ Performing data analysis...")
        break
    else:
        print("⚠️ Invalid input. Enter 'y' or 'n'.")

# --- Statistical Calculations ---
if numbers:
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)

    # Median
    n = len(sorted_nums)
    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

    # Mode
    counter = Counter(sorted_nums)
    max_value, freq = counter.most_common(1)[0]
    mode = max_value if freq > 1 else "No mode (all values unique)"

    # Variance & Standard Deviation
    variance = np.var(numbers)
    std_dev = np.std(numbers)

    print("\n--- Statistical Summary ---")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

print("\n📊 Analysis Complete. Thank you for using the tool!")
