''' This program allows a user to acess two different financial calculators: an investment calculator and a home loan calculator'''

import math

print("investment - too calculate the amount of interest you'll earn on your investment ")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

#The user is asked to choose which financial calculator they want to use. 
# if they choose investment then they have to choose between simple and compound.

user_choice = input("Enter either 'investment' or 'bond'from the menue above to proceed   ")
if user_choice == 'INVESTMENT'or user_choice == 'Investment'or user_choice == 'investment':
  principle = float(input("Enter the amount to be deposited:  "))  
  interest_rate= float(input("Enter the interest rate:  "))  
  interest_rat=  interest_rate/100 
  years=  float(input("Enter the number of years for investment:  "))  
  interest= input("Enter your choice of simple or coompound interest  ")
  if interest== 'simple':
    Amount=principle*(1+(interest_rat * years))
    print(f"\nYou will earn an amount of {Amount} per year.")
  else:
     interest == 'compound'
     Amount= round(principle * math.pow((1+interest_rat),years),2)
     print(f"\nYou will earn an amount of  {Amount}  per year.")
  
 # if the user choose a home looan calculator
   
elif user_choice == 'BOND'or user_choice == 'Bond'or user_choice == 'bond':
    House_val = float(input("Enter the present value of the house:   "))  
    monthly_rate= float(input("Enter the interest rate: "))    
    monthly_rat= (monthly_rate/100)/12
    month=  float(input("Enter the number of month you plan to repay the bond:  ")) 
    repay=round(((monthly_rat * House_val )/(1-(1+monthly_rat)**(-month))),2)
    print(f"\nYou will have to pay an amount of {repay} each month.")

# if the user did not type a valid input, this msg will appear
else:
   print("Sorry! you did not make a choice. Try again") 











