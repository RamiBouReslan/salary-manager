action = "yes"
utility = ""
monthList = []

while action != "no" and action == "yes":
    
    month = input("Specify which month the salary is for: ")
    salary = int(input(f"Enter your salary for {month}: $ "))
    months = {
        "month" : month,
        "salary" : salary,
    }
    bills = []
    bill = {}
    newCategory = input("Is there any additional bill category other than savings, rent, and electricity.(Enter 'yes' or 'no'): ")
    if newCategory != "no" and newCategory == "yes":
        utilities = ["Savings","Rent","Electricity"]
        while newCategory != "no" and newCategory == "yes":
            utility = input("Enter new bill category: ")
            utilities.append(utility)
            newCategory = input("Is there any additional bill category other than savings, rent, and electricity.(Enter 'yes' or 'no'): ")
         
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

  
    action = input("Want to add a new month? (Enter 'yes' or 'no'): ")


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

        print (f"The combined expenses for {months['month']} is {expenses}. ")
        print (f"The remaining amount from your salary for {months['month']} is {value}. ")
        print (f"The estimated yearly cost of rent based on {months['month']}'s budget is: {yearRent}")
        print (f"The estimated yearly cost of electricity on {months['month']}'s budget is: {yearElectricity} ")
        print (f"The square of {months['month']}'s salary is ${(months['salary'])**2} (For Fun).")
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
    print (f"The square of your yearly estimated salary is {yearlySalary**2} (For Fun).")
    print ("---------------------------------------------------------------------------------------------------")      


else:
    print (" --ERROR-- Couldn't calculate yearly budgets. \nYou've entered more than 1 year worth of months. ")
    print ("---------------------------------------------------------------------------------------------------")   

condition = input("Do you have any salary modifications?(Enter 'yes' or 'no'): ")

while condition == "yes" and condition != "no":
    monthChange = input ("Enter which month you wish to modify its salary: ")
    salaryChange = int(input (f"Enter the amount you wish to add on the salary of {monthChange}: $"))
    newExpenses = 0
    newCosts = {}
   
    for y in range(len(monthList)):
        edit = monthList[y]
        if monthChange == edit["month"]:
            newSalary = salaryChange + edit["salary"]
            print (f"\nRevised Month: {monthChange} \nUpdated salary: ${newSalary}.\n")
            
            for item in edit["Bills"]:
                itemKey = list(item.keys())
                for k in itemKey:
                    item[k] = (item[k]/edit["salary"])*newSalary
                    if k == "Electricity" or k == "Rent":
                        newCosts[k] = (item[k]*12)
                    if k != "Remainder":
                        newExpenses += item[k]
                        print(f"The updated {k} budget is {item[k]}") 

            edit["salary"] = newSalary   
                                       
            print (f"The combined updated expenses for {edit['month']} is {newExpenses}. ")
            print (f"The remaining amount from your updated salary for {edit['month']} is {item[k]}. ")
           
            for n in newCosts:
                print (f"The estimated yearly cost of {n} based on {edit['month']}'s budget is: {newCosts[n]}")
               
            print (f"The square of {edit['month']}'s salary is ${(edit['salary'])**2} (For Fun).")
            print ("---------------------------------------------------------------------------------------------------")
        
    condition = input("Do you have any salary modifications?(Enter 'yes' or 'no'): ")    
  