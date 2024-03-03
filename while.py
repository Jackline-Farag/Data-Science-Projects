counter=0
Total=0
print('''You will be asked to enter a number and an average of the numbers entered is calculated, 
entering -1 will result in quiting the program\n''')

# The while loop will continue until the number eentered is -1
while True:
    number= float(input("Enter a number (-1 will quit the program):  "))
    if number!=-1:
        Total=Total+number
        counter+=1
        
    else:
 # This will display the average of the numbers entered by the user 
        Average=Total/counter
        print (f"The average of the numbers entered is {Average}")
        break
