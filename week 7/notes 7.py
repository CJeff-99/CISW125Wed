#  What is a Look
# # # # # A loop repeats code

# # # # #repeat this loop 3 times
# for number in range(5):
#     #Print Hello each time the loops runs
#     print("Hello")


# # # #While Loops
# # # #A while loop repeats while a condition is true
# # # number = 1 # This is the starting point

# # # #Keep looping while number is less than or equal to 5
# # # while number<=5 #This is essentailly, where will it stop
# # #     print(number)
# # #     number+=1 #Add 1 to number after each loop
# # # # I want to start at 0, count to 50, and get ther by increments of 5
# # # number2=0
# # # while number2<=50:
# # #     print(number2)
# # #     number2+5

# # #A while loop is useful when you wanty to keep asking until the user gives a valid answer 
# # age=int(input("enter your age")) 

# # # keep looping if the age is less than 1 or greater than 120
# # while age  < 1 or age >120:    #The loop only runs is one of the conditions is true
# #     #Tell the user, invalid input
# #     print("Invalid Age")

# #     #Ask the user to enter their age again
# #     age=int(input("enter your age")) 
# # #This runs after the loop finishes
# # print("Thank you")


# #FOR LOOP 
# #A for loop works through items one at a time

# # #Create a list containing 3 games
# # games= ["Gears of war", "Halo", "Myth"]
# # #take one item from the games list at a time
# # for game in games:
# #     #print the current game
# #     print(game)
# # #Each time the loop repeats, game hold the next item in the list

# # #Range
# # #Range() creates a sequence of numbers
# # #Starts at 2 and stops right before 8
# # for number in range(2,8): 
# # #(Starting number, stop right before this number)
# #     #print the current number
# #     print(number)
# #     #Remember the ending number in range() is not included 

# #we can also preform calculations inside the loop:
# #Loop through the numbers 2 through 7
# # for number in range(2,8):
# #     #multiply the number by itself
# #     square=number*number 
# #     #print the squared number
# #     print(square)


# #Looping through a string 
# #sore a name inside the string
#name="Jogin"
# #Take one character from the string at a time 
#for letter in name:
#    print(letter)
# #This works very similar to how we loop through a list


# #USING BREAK
# #Break stops a loop early

# #Loop through number 1-10
# for number in range(1,11):
#     #print the current number
#     print(number)
#     if number==5:
#     #once number is equal to 5, loop will stop 
#     break

#Nested loop
#nested loop is a loop inside another loop

#outer loop run through 1,2,3
# for number in range(1,4):
#     #inner loop also runs through 1,2,3
#     for number2 in range(1,4):
#         print(number, number2)

#Choosing the right loop?
#Use a while loop when repetition depends on a condition 

#Keep looking while answer is not yes
# while answer !="Yes":
#     #Ask the user again
#     answer=input("Enter yes:")

# use a for loop when working through items
#Go through each item in the list
# item=["apples", "oranges", "grapes"]
# for item in items:
#     #print the current item
#     print(item)

# #use FOR with Rangew() when woring through numbers
# for number in range(1,11):
#     #Print the current number
#     print(number)
