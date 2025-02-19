month = input("Specify which month the salary is for: ")

salary = int(input(f"Enter your salary for {month}: "))

utilities = []
utility = ""
divided_percentage = []
 
while utility != "stop":
    utility = input("Enter allocated utility: ")
    if utility != "stop":
        percentage = int(input(f"Enter the pecentage allocated for {utility}: %"))
        utilities.append(utility)
        divided_percentage.append(percentage) 
    else:
        utilities.append ("Remainder")
        divided_percentage.append(100 - sum(divided_percentage))
        break



