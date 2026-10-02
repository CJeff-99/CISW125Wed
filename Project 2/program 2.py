first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
if first_number>second_number:
    result= first_number* second_number 
    print(f"The product of {first_number} and {second_number} is: {result}")    
else:
    result= first_number+ second_number 
    print(f"The sum of {first_number} and {second_number} is: {result}")