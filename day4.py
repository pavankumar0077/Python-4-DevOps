# Input from user
# a = input("Enter a name: ")
# print(f"User enter name : ", a)

# b = int(input("Enter a number: "))
# print("User entered number : ",b)


# Loops -- If condition
age = int(input("Enter your age :"))
if age >= 18:
    print("User is Adult")
else:
    print("User is minor")


# Multiple If else conditions
score = int(input("Enter your score: "))
if score >= 90:
    print(f"Grade : A", score)
elif score >=80:
    print("Grade B", score)
elif score >= 70:
    print("Grade C", score)
else:
    print("Grade D", score)


# Nested if conditions
x = 16
y = 5
if x > y:
    print("X is greater than y")
    if x > 15:
        print("X is also greater than 15")
    else:
        print("X is not greater than 15")
else:
    print("X is not greater than y")


# Loops - For Loop -- using for each loop
fruits = ['apple','banana','cherry']
for item in fruits:
    print(f"items are ", item)


# For loop
numbers = [1,2,3,4,5,6,7]
for i in numbers:
    print(i)


# While Loop
count = 0
while count < 5:
    print(count)
    count += 1
    # count = count + 1


# For loop with Range
for j in range(10):
    if j == 5:
        break
    print(j)

for k in range(6):
    if k == 5:
        continue
    print(k)

# For loop in Dictory
person = {'name':'Pavan', 'age':24, 'city':'Hyd'}
for key,value in person.items():
    print(f"{key}:{value}")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed without break")