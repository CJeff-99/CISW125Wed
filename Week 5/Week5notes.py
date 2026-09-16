# #What is a boolean?     
# #A boolean value is either true or false 
# #Ex
# # print(5<10)
# # print(5>10)
# # print(3>=7)
# # print('cat'=='dog')

# answer=input("Do you want to contine? (yes or no)").lower()
# # if answer =="yes":
# #     print("continuing the program....")
# # elif answer=="no":
# # else:
# #     print("Okay, exiting now.")



# #comparison Operators
# # == equal to 
# # !+= not equal to
# # > greater than
# # < less then 
# # <= less then or equal to
# # >= greater than or equal to 

# # score= 85 
# # print(score>75)
# # print(score==75)
# # print(score!=85)


# #How do we compare 3 values?
# #We can compare 3 or more values with "and" "&" 'or'
# # temp= 72
# # if temp >=68 and temp <= 75:
# #     print("Comfy room temp")
# #When using and, both conditions both conditions must be trut
# #When using OR, at least one condition must be true

# # day="Saturday"
# # is_holiday=False
# # if day=="Saturday" or day=="Sunday" or is_holiday
# #     print("You dont have class today")


# # score=75
# # if score <= score <90:   # score >= 60 and score is < 90
# #     print("Medicore grade")



# #Give a conditional progrma that prints out shipping cost depending on total price
# total= float(input("enter your total order:"))
# if total<25:
#     print("Shipping is 10$")
# elif total< 50:
#     print("Shipping is 5$")
# else:
#     print("Shipping is free!")


list1=[1,2,3]
list2=[1,2,3]
list3=list1

print(list1==list2)
print(list1 is list2)
print(list1==list3)
print(list1 is list3)
#== compare values and contents 
# is, compare identity (are they literally the same object)
             