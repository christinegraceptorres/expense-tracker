# Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Christine Grace Torres
# Developed a menu-driven Expense Tracker using loops and conditional statements to record expenses, calculate totals and tax, and monitor the user's budget.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0

while True:

    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses", "\t" * 2, "(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")


    choice = input ("Choose 1-4: ")
    
    if choice == "1":
        amount = float (input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print ("  Huge expense - are you sure?")
        elif amount > 100:
            print ("  Big expense.")
        elif amount > 50:
            print ("  Moderate expense.")
        else:
            print ("  Small expense.")


    elif choice == "2":
        print ("  Coming soon: the tracker can't remember each item yet.")


    elif choice == "3":

        # Computations :)
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax

        over_budget = total > budget
        left = budget - total

        print(f"  Expenses: \t\t {count}")
        print("  Subtotal:", "\t" * 2, f"${subtotal}")
        print(f"  Tax ({tax_percent}%)\t\t ${tax}")
        print(f"  Grand total:\t\t ${total}")
        if over_budget:
            print(f"  Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"  Careful: only ${left} left.")
        else: 
            print(f"  Within budget. ${left} left.")


    elif choice == "4":
        # Me <3
        print(f"Goodbye, {name}!")
        break


    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Christine Grace Torres | Installment 5")
print("=" * 40)