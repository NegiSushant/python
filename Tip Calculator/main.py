print("Welcome to the TiP CaLcUlAtOr.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
bill_with_tip = bill * tip / 100
total_bill = bill_with_tip + bill
bill_with_split = round(total_bill / split, 2)
bill_with_split = "{:.2f}".format(bill_with_tip)
print(f"Each person should pay: ${bill_with_split}")
