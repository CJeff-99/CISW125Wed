# #Whats the difference between a int and a float?
# #an int is a whole number, while a float is a number that has a decimal point. For example, 5 is an int, while 5.0 is a float.
# x=30 #int value
# y=2.5 #float value
# print(x,type(x))
# print(y,type(y))


# print(x//y)   #// floor division, will give whole number value
# print(x/y)   #/ regular division, will give float (decimal) value


# user_text=input("type something: ")
# print(f"Hello, {user_text}")



# #user input always automatically converts input to string
# #regardless of waht we have typed
# age=int(input("What is your age: "))  #asks for age, makes input string
# age_int=int(age_text)  #converting variable on line 22 into an INT
# print(age,type(age))

# #string is text 
# # messge + "CISW 125"
# # @print(message, type(message)) 

# word="Python"
# print(word[0])#this selects the first letter of my word
# print(word[1])#this selects the second letter of my word
# print(word[2])#this selects the third letter of my word
# print(word[3])#this selects the fourth letter of my word
# print(word[4])#this selects the fifth letter of my word
# print(word[5])#this selects the sixth letter of my word

#slicing is when we want to print a range from string text
# print(word[0:3])
#start:end means start at and stop before end              #ctrl plus / to comment out multiple lines of code

#built in python functions
#.upper(), this converts all letters in a string to uppercase
#.lower(), this converts all letters in a string to lowercase
# phrase="Hello, world"
# print(phrase.upper())
# print(phrase.lower())


fruits=["apple","banana","watermelon"]
numbers=["10","30","500"]
mixed=[10,"score",3.9]


print(fruits[0]) #this will print the first item in the list
print(fruits[0:2]) #this prints the first two items
#to add to a list, we append the list name
fruits.append("lemon")
print(fruits)

print(5**5)


