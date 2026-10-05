# Expense Tracker - Installment 3: The Tracker Does Math
# Author: Christine Grace Torres
# Computes subtotal, average, tax, grand total, budget, and over-budget status.
print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense", "\t" * 2,  "(coming soon)")
print("\t[2] View all expenses", "\t" * 2, "(coming soon)")
print("\t[3] Show total spent", "\t" * 2, "(coming soon)")
print("\t[4] Exit", "\t" * 3, "(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses. \n")

# User Inputs for items and amounts..
subtotal = 0
item1 = input("First Expense? ")
amount1 = float (input("Amount? "))
subtotal += amount1
item2 = input("Second Expense? ")
amount2 = float (input("Amount? "))
subtotal += amount2
average = subtotal / 2

# Tax & Budget Inputs section..
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Computations :)
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

over_budget = total > budget
left = budget - total

# For Output part :D
print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:", "\t" * 2, f"${amount1}")
print(f"\t- {item2}:", "\t" * 2, f"${amount2}")
print("Subtotal", "\t" * 3, f"${subtotal}")
print("Average:", "\t" * 3, f"${average}")
print(f"Tax ({tax_percent}%)\t\t\t ${tax}")
print(f"Grand total:\t\t\t ${total}")
print(f"Over budget?\t\t\t {over_budget}")
print(f"Left in budget:\t\t\t ${left}")

# Me <3
print("-" * 40)
print("Made by Christine Grace Torres | Installment 3")