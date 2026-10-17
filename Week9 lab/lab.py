# with open("Week9 lab/words.txt","r") as file:
#     contents=file.read()
#     print(contents)
# This is task 2



# with open("Week9 lab/words.txt","a") as file:
#     file.write(" Hamburger")
#this is task 3


# with open("Week9 lab/words.txt","r") as file:
#     contents=file.read()
#     print(contents)
# #this is task 4

user_input=input("What is your name? ")
with open("Week9 lab/words.txt","a") as file:
     file.write("\n" + user_input)

