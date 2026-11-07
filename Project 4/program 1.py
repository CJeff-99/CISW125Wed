sandwich=input("What kind of sandwich would you order?" )
bread=input("What kind of bread would you like?")
if sandwich=="Roast Beef":
    if bread=="Sour Dough":
        print("You ordered a Roast Beef on Sour Dough.")
    else:
         print("Thats a great choice, but we don't have that option. We only have Sour dough for Roast Beef sandwiches.")
else:
    print("We only have Roast Beef sandwiches at this time. Please come back later for other options.")