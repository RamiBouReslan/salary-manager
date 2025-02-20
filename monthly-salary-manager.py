action = "yes"
utility = ""
monthList = []

while action != "no":
    
    month = input("Specify which month the salary is for: ")
    salary = int(input(f"Enter your salary for {month}: $ "))
    months = {
        "month" : month,
        "salary" : salary,
    }
    bills = []
    bill = {}
    newCategory = input("Enter 'no' if there isn't any additional bill category other than savings, rent, and electricity.")
    if newCategory != "no":
        while newCategory != "no":
            utilities = ["Savings","Rent","Electricity"]
            utility = input("Enter new bill category: ")
            utilities.append(utility)
            newCategory = input("Enter 'no' if there isn't any additional bill category other than savings, rent, and electricity.")
         
        for category in utilities:
            percentage = int(input(f"Enter the percentage allocated to {category}: % "))
            bill[category] = salary * (percentage/100) 
        bill["Remainder"] = salary - sum(bill.values()) 
        bills.append(bill)
        months ["Bills"] = bills
        monthList.append(months)
        
    else:
        utilities = ["Savings","Rent","Electricity"]

        for category in utilities:
            percentage = int(input(f"Enter the percentage allocated to {category}: % "))
            bill[category] = salary * (percentage/100) 
        bill["Remainder"] = salary - sum(bill.values()) 
        bills.append(bill)
        months ["Bills"] = bills
        monthList.append(months)
        # print (bill) 
  
    action = input("Want too add a new month? (Enter no if not): ")
print (monthList)


#     # divided_percentage = []
    
#     while utility != "stop":
#         utility = input("Enter allocated utility: ")
#         if utility != "stop":
#             percentage = int(input(f"Enter the pecentage allocated for {utility}: %"))
#             utilities.append(utility)
#             divided_percentage.append(percentage) 
#         else:
#             utilities.append ("Remainder")
#             divided_percentage.append(100 - sum(divided_percentage))
#             break

#     budget = []

#     for i in range(len(utilities)):
#         amount = salary * divided_percentage[i]/100
#         budget.append(amount)
#         if utilities[i] != "Remainder":
#             print(f"The budget for {utilities[i]} is ${budget[i]}.")
#         else:
#             break
# print (f"The combined budget of the utilities is ${sum(budget)-amount}.")
# print (f"The remainder of your salary for this month is ${amount}.")