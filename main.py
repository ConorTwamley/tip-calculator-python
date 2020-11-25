#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator\n")
bill = input("What was the bill total? \n")
percentage = input("What percentage would you like to give? 10, 12 or 15? \n")
people = input("How many people to split the bill? \n")

bill_float = float(bill)
percentage_float = float(percentage) /100
tip_percentage = percentage_float + 1
people_int = int(people)


tip_result = round((bill_float / people_int) * tip_percentage)

print(f"Each person should pay: ${tip_result}")
