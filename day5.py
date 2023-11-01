def greet(name):
    print(f"Hello, {name}!!")

greet("Pavan")
greet("Kumar")



def addition(x,y):
    return x+y

print(f"additon of x and y is : ",addition(2,5))
print(addition(34,5555))


def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 !=0

def square(num):
    return num ** 2

# Test the functions
num = int(input("Enter a number : "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd")
print(f"The square of {num} is {square(num)}.")