# ------------------------------
# 💰 Expense Tracker
# ------------------------------
expenses = [
    {"amount": 200, "category": "Food", "note": "Lunch"},
    {"amount": 150, "category": "Transport", "note": "Taxi"},
    {"amount": 300, "category": "Food", "note": "Dinner"},
    {"amount": 100, "category": "Entertainment", "note": "Movie"},
    {"amount": 250, "category": "Transport", "note": "Train tickets"}
]

# Calculate totals for each category
totals = {}
for exp in expenses:
    cat = exp["category"]
    totals[cat] = totals.get(cat, 0) + exp["amount"]

print("\n--- Expense Summary by Category ---")
for cat, total in totals.items():
    print(f"{cat}: ₹{total}")

print("\n--- Visual Representation ---")
for cat, amount in totals.items():
    print(f"{cat}: {'⬜' * (amount // 50)}")
