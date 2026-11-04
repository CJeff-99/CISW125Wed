# Favgames=["halo", "Gears", "Minecraft"]

# print(Favgames[0])
# print(Favgames[1])
# print(Favgames[2])

#Using Len() with a list 
#We can use Len() to find out how many total items are in a list  
# print(len(Favgames))

#Adding items to a list
#Append adds to the end of the list
#insert() adds an item at a specific postition 
# Favgames.append("Dark Souls")
# print(Favgames)

# Favgames.insert(o,"Marvel Rivals")
# print(Favgames)


#Common list methods

#Count() counts how many times a value appears
#Remove() Removes a specific item 
#Sort() puts the list in a sorted order
#Reverse flips the current ordetr of the list


# Favgames=["halo", "Gears", "Minecraft", "Mario Kart"]

# print(Favgames.count("Mario Kart"))

# #remove Example
# Favgames.remove("Mario Kart")
# print(Favgames)

# #sort 
# Favgames.sort()
# print(Favgames)


# #Reverse Ex
# Favgames.reverse()
# print(Favgames)


# Favgames=["halo", "Gears", "Minecraft", "Mario Kart"]

# #Loop through the items within my list
# for games in Favgames:
#   print(games)




#Dictionaries Storung Labeled Information
#A dictionary sores data in key value pairs
#Dictionaries are useful when a label matters more than position


#Make a dictionary that is called player stats
player_stats={
  #Dictionary values must be health, mana, level, gold
  #word:value
  "Health": 100,
  "Mana": 40,
  "level": 15,
  "Gold": 25,
}

#Lists vs Dictionaries 
#use a list when a order matters and you wat a collceiton of items
#Dictionary is used when labels matter and you wat ot look things up by name 

#Access  Dictionary
# print(player_stats["Health"])

# #Add and update dictionary values?
# #You can adda new key-value pair by assigning a vlue to a new key
# #You can also update an existing value or increase it

# # player_stats["Strength"]=50
# # player_stats["Health"]=200
# # player_stats["Health"]+=200
# # print(player_stats)

# #keys() and Vlaues()

# #KEYS shoew all dictionaty values
# #Values sjpw all dictionary vlaues 


# #loop through the keys
for stats in player_stats.keys():
   print(stats)

# #looping through values
# for values in player_stats.values():
#   print(values)


  # #Loop through both keys and values
  # for stats, values in player_stats.items():
  #   print(f"{stats}: {values}")


#Nested Dictionaries
# students={
#     "oo1"{
#       "Name": "Ana"
#       "Major": "Programming",
#       "credits": 6
#     }
#     "002":{
#       "Name": "Joe"
#       "Major": "Cyber",
#       "credits": 15
#       }
# }

# #Access nested dictionary Vlaues?
# #To access nested data go


# print(students["002"]["Major"])



# #Nested strucutes can mix lists and dicitonaries 
# #programs often combine mulitple data structuree together
# #An Inner dictionary can contain a list as one of its values
# students={
#     "005"{
#       "name":"Rickey",
#       "Classes":["Math", "Hacking", "English"]
#     }
# }