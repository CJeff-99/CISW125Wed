total_sum = 0
count = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    number = float(user_input)
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
    print(f"Sum: {total_sum}, Count: {count}, Average: {average}")
else:
    print("No numbers entered.")