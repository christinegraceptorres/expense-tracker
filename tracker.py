# Expense Tracker - Installment 4: The Tracker Makes Decisions
# Author: Christine Grace Torres
# Log two expenses, checks their sizes, gives a warning if both are big, and tells you if you stayed within your budget.
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
item1 = input("First expense? ")
amount1 = float (input("Amount? "))
subtotal += amount1
# Checking of inputted amount 1.
if amount1 > 200:
    print ("  Huge expense - are you sure?")
elif amount1 > 100:
    print ("  Big expense.")
elif amount1 > 50:
    print ("  Moderate expense.")
else:
    print ("  Small expense.")

item2 = input("Second expense? ")
amount2 = float (input("Amount? "))
subtotal += amount2
average = subtotal / 2
# Checking of inputted amount 2.
if amount2 > 200:
    print ("  Huge expense - are you sure?")
elif amount2 > 100:
    print ("  Big expense.")
elif amount2 > 50:
    print ("  Moderate expense.")
else:
    print ("  Small expense.")

# Checking if both amounts are over 100.
if amount1 > 100 and amount2 > 100:
    print ("  Two big expenses in a row - slow down!")

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
print("Subtotal:", "\t" * 3, f"${subtotal}")
print("Average:", "\t" * 3, f"${average}")
print(f"Tax ({tax_percent}%)\t\t\t ${tax}")
print(f"Grand total:\t\t\t ${total}")
# Checking if over budget, near the budget limit, or within the budget.
if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9: 
    print(f"Careful: only ${left} left.")
else: 
    print(f"Within budget. ${left} left.")

# Me <3
print("-" * 40)
print("Made by: Christine Grace Torres | Installment 4")