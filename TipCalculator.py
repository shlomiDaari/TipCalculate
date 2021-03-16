#Tip calculator!! 
bill_num = input("What is the bill? ")
print("The bill is: " + bill_num)
numOf_people = input("To how many people do you want to split the bill? ")
#Calculate to how many people to split the Bill before the Tip!
bill_each_one = float(bill_num)/float(numOf_people)

Tip = input("How much Tip precent do you want to give? ")

#Add the Tip to each one Bill

bill_each_one += ((float(Tip)/float(bill_each_one))*100)   
print(f"Each person need to Pay {bill_each_one}$")    