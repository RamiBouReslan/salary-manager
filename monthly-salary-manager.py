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
    newCategory = input("Enter 'no' if there isn't any additional bill category other than savings, rent, and electricity. ")
    if newCategory != "no":
        utilities = ["Savings","Rent","Electricity"]
        while newCategory != "no":
            utility = input("Enter new bill category: ")
            utilities.append(utility)
            newCategory = input("Enter 'no' if there isn't any additional bill category other than savings, rent, and electricity. ")
         
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


for i in range(len(monthList)):
    months = monthList[i]
    print (f"\nMonth: {months['month']} \nSalary: ${months['salary']}.\n")
    expenses = 0
    for type in months["Bills"]:
        for key, value in type.items():
            if key != "Remainder": 
                if key == "Rent":
                    yearRent = value*12
                elif key == "Electricity":
                    yearElectricity = value*12
                print(f"The {key} budget is {value}")
                expenses += value 

        print (f"The combined expences for {months['month']} is {expenses}. ")
        print (f"The remaining amount from your salary for {months['month']} is {value}. ")
        print (f"The estimated yearly cost of rent based on {months['month']}'s budget is: {yearRent}")
        print (f"The estimated yearly cost of electricity on {months['month']}'s budget is: {yearElectricity} ")
        print (f"The square of {months['month']}'s salary is ${(months['salary'])**2} (For Fun) ")
        print ("---------------------------------------------------------------------------------------------------")


totalSalary = []
totalRent = []
totalSavings = []
totalElectricity = []

if len(monthList) <= 12:
    for i in range(len(monthList)):
        months = monthList[i]

        for kind in months["Bills"]:
            for keys,values in kind.items():
                if  keys == "Savings":
                    totalSavings.append(values)
                elif keys == "Rent":
                    totalRent.append(values)
                elif keys == "Electricity":
                    totalElectricity.append(values)
    
        totalSalary.append(months['salary'])  
        yearlyRent = 12 * sum(totalRent)/len(totalRent) 
        yearlySavings = 12 * sum(totalSavings)/len(totalSavings)
        yearlyElectricity = 12 * sum(totalElectricity)/len(totalElectricity)
        yearlySalary = 12 * sum(totalSalary)/len(totalSalary)
    
    print (f"\nThe yearly average budgets will be estimated according to the total number of months entered: {len(totalSalary)}")
    print (f"The estimated averager yearly salary is ${yearlySalary}")
    print (f"The estimated averager yearly budget for savings is ${yearlySavings}")   
    print (f"The estimated averager yearly budget for rent is ${yearlyRent}") 
    print (f"The estimated averager yearly budget for electricity is ${yearlyElectricity}") 
    print (f"The square of your yearly estimated salary is {yearlySalary**2}")
    print ("---------------------------------------------------------------------------------------------------")      


else:
    print (" --ERROR-- Couldn't calculate yearly budgets. \nYou've entered more than 1 year worth of months. ")
    print ("---------------------------------------------------------------------------------------------------")   
