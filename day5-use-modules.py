# Here we are calling math ops class as a module and using it
import math_operations

a = math_operations.add(5,7)
print(a)


print(f"Sub value of x and y is : ", math_operations.sub(7,2))

b = math_operations.div(4,0)
print(b)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
c = math_operations.mul(x,y)
print(c)

result_add = math_operations.add(1,2)
result_sub = math_operations.sub(2,1)
result_mul = math_operations.mul(3,4)
result_div = math_operations.div(5,3)

print(f"Addtion : {result_add}")
print(f"Sub : {result_sub}")
print(f"Mul : {result_mul}")
print(f"Div : {result_div}")