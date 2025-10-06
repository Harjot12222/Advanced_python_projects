# ------------------------------
# 📊 Number Statistics Calculator
# ------------------------------
from collections import Counter
import numpy as np

numbers = []

# Collect user input
while True:
    user_choice = input("Do you want to add a number to the list? (y/n): ").lower()
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
            print("✅ Calculation complete.")
        break
    else:
        print("⚠️ Invalid input. Enter 'y' or 'n'.")

# Perform calculations
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

    # Output
    print("\n--- Statistical Summary ---")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
