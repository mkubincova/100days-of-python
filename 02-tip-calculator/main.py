print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip = (bill / people) / 100 * percentage
bill_with_tip = (bill / people) + tip

print(f"Each person should pay: ${'{:.2f}'.format(round(bill_with_tip, 2))}")