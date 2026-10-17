#How to write read and edit files in python
#Common modes when using Files
# 
# "r" read only
#You cna read this file, but cnat change
# Error if file doesnt exist

#"w" =write
#Create the file if it doesnt exist
# Overwrites the file if it does exist deletes old content

#"a" = append
# Creates the file if it doesent exist 
# Adds new text to the file and does not delete existing content

#with open("Filename,"mode")
# with open ("Week9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)

# with open("Week9/stuff.txt","w") as file:
#      file.write("Hello!\n")

#once we leave the indentation block file auto closes

#Reading from a file 
#Method a: Read the whole file at once
# with open("Week9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)


#Method B read line by line using a for loop
# with open("Week9/stuff.txt","r") as file:
#     for line in file:
#         print(line)

#Appending to a file (Adding to a file)
#Appending add to the end of a file without deleting whats already there
with open("Week9/stuff.txt","a") as file:
    # file.write("\n")
    file.write("This should appear at the very end, cause we used mode A")
#we used