sandwich=input("What kind of sandwich would you order?" )
bread=input("What kind of bread would you like?")
if sandwich=="turkey":
    if bread=="wheat":
        print("You ordered a turkey on wheat bread.")
    else:
         print("Thats a great choice, but we don't have that option. We only have wheat bread for turkey sandwiches.")
else:
    print("We only have turkey sandwiches at this time. Please come back later for other options.")