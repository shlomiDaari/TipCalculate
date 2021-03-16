#Tip calculator!!
print("Welcome to Tip Calculate") 
total_bill = float(input("What is the total bill? "))
print(f"The total bill is:  {total_bill}")
numOf_people = float(input("To how many people do you want to split the bill? "))
tip = float(input("How much precent of Tip would you like to give? "))
tip_precent = float(tip/100)
tip_amount = float(tip_precent*total_bill/numOf_people)
total_bill_with_precent = round(total_bill/numOf_people + tip_amount)
message = f"Each one should pay {total_bill_with_precent}, including the Tip!"
print(message)

