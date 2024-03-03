'''This program calculates the total stock of a cafe'''

Menu=["Latte","Espresso","Cappuccino","Hot Chocolate","Green Tea"]


Stock= {'Latte':30,'Espresso':50,'Cappuccino':20,'Hot Chocolate':15,'Green Tea':25}

Price= {'Latte':5.00,'Espresso':5.00,'Cappuccino':3.00,'Hot Chocolate':4.00,'Green Tea':6.00}

Total_stock=0
for items in Menu:
    item_value=(Stock[items]*Price[items])
    print(f"The stock of",items,"is worth $",item_value)
    Total_stock=Total_stock+item_value
print(f"\nThe Total stock of the cafe is worth $",Total_stock)
    
       