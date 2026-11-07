# cart=["Oranges", "cereal", "Coffee", "Milk"]
# # print(len(cart ))
# # print(cart[0])
# # print(cart[3])
# # cart.append("Tuna")
# # print(cart)
# # cart.insert(1, "sausages")
# # print(cart)


# # print(cart.count("Oranges"))

# # # cart.remove("Milk")
# # # print(cart)


# # # cart.sort()
# # # print(cart)  #Changed order of items

# # cart.reverse()
# # print(cart)

# store_inventory={
#     "Apples": 55,
#     "cabbages": 3000,
#     "Captain Crunch": 20,
#     "Peaches": 15,
#     "Borax": 30,
# }
# # print(store_inventory["Apples"])
# store_inventory["Raisins"]=5
# store_inventory["Apples"]+=10
# print(store_inventory)

# # for items in store_inventory.keys():
# #     print(items)

# # for amounts in store_inventory.values():
# #     print(amounts)

# for inventory, amounts in store_inventory.items():
#     print(f"{inventory}: {amounts}:")


Customers={
    "587":{
        "Name": "Billy",
        "Items bought": ["Oranges", "apples", "Coffee"],
        "Total spent": 16.50
    },
   
    "2568":{
        "Name": "Samantha",
        "Items bought": ["Crayons", "bananas", "shirts"],
        "Total spent": 26.35
    }
}
print(Customers["587"]["Items bought"])
print(Customers["2568"]["Total spent"])