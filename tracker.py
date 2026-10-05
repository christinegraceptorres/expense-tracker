# Expense Tracker - Installment 2: Talking to the User
# Author: Christine Grace Torres
# Shows the landing page, asks for two expenses, prints a summary.
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

item1 = input("First Expense? ")
amount1 = float (input("Amount? "))
item2 = input("Second Expense? ")
amount2 = float (input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:", "\t" * 2, f"${amount1}")
print(f"\t- {item2}:", "\t" * 2, f"${amount2}")
print("Total Spent:", "\t" * 3, f"${total}")
print("Average:", "\t" * 3, f"${average}")

print("-" * 40)
print("Made by Christine Grace Torres | Installment 2")