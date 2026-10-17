finishers = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Daniel", "Ricky Bobby"]

print("--- Official Race Results ---")

for place, runner in enumerate(finishers, start=1):
    if place == 1:
        suffix = "st"
    elif place == 2:
        suffix = "nd"
    elif place == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    print(f"{place}{suffix} Place: {runner}")