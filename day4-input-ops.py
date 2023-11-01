# Taking user input
user_input = int(input("Enter an Integer : "))


# Checking if the number is even or odd
if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is odd number ")

# Using a for loop to print numbers from 1 to user-input number
print("Numbers form 1 to ", user_input)
for i in range(1, user_input + 1):
    print(i)



