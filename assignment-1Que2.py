###  2. Write a python program to compute a person's income tax. ###

print(" 2. Write a python program to compute a person's income tax. ")

### inputs from user ###
gross_income = float(input("Enter the Gross Income to the nearest penny : "))
dependents = int(input("Enter the number of Dependents : "))

### calculation of tax ###
Taxable_income = gross_income - 10000 - (3000*dependents)
Tax=(Taxable_income*20)/100

if Tax<0:
    print("Your income tax is 0$")
else:
    print(Tax)