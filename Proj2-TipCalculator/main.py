print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))
total_bill_per_person = (bill + (bill * (tip / 100))) / people
res = "{:.2f}".format(total_bill_per_person)
print(f"Final bill for each person: ${res}")
