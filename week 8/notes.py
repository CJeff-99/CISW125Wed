#Count down timer
# seconds=int(input('Enter the time you want to countdown from:'))
# while seconds>=0:
#     if seconds==3:
#         print('Almost there')
#     elif seconds ==0:
#         print("Times up")
#     seconds-=1


#Bank Program
# balance= 1000
# while True:
#     print(f"{balance},Balance")
#     choice=input("Deposit,withdraw or exit").lower()
#     if choice=="Deposit":
#         amount=float(input("Amount:"))
#         balance+=amount
#     elif choice=="Withdraw":
#         amount=float(input("How much money do you want to take out?"))
#         if amount>balance:
#             print("Not enough funds")
#         else:
#             balance-=amount
#     elif choice =="exit":
#         break
# print(f"Final balance: {balance}")


#Random number generator
# print("Guess the number:")
# target=4
# while True:
#         guess=int(input("Enter your guess"))
#         if guess<target:
#                 print("Too low")
#         elif guess>target:
#                 print("Too high")
#             else:
#                 break
# print("Correct")


#create a grocery list
#make a empty list
# list=[]
# while True:
#     #ask the user if they want to add an item to list
#     userInput=input("Do you want to add to the list?").lower()
#     if userInput=="yes":
#         item=input("Enter the item to add")
#         list.append(item)
#     elif userInput=="no":
#         break
#     else:
#         print("Invalid input")

