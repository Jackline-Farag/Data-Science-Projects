counter=0
Total=0
print('''You will be asked to enter a number and an average of the numbers entered is calculated, 
entering -1 will result in quiting the program\n''')
while True:
   
    number= float(input("Enter a number:  "))
    if number!=-1:
        Total=Total+number
        counter+=1
        
    else:
        Average=Total/counter
        print (f"The average of the numbers entered is {Average}")
        break
