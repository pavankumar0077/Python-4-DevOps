print("Hello Word")


a = 234
b = 45.4
c = "Pavan"
d = "Pavan's"
e = """ This is the world of 
        AI and scifi"""
is_valid = True
is_working = False


print(type(a))
print(type(b))
print(type(c))
print(type(is_valid))


print(d)
print(e)
print(is_valid)
print(is_working)


# List (Mutable -- We can change the values)
f = [1,2,3,'Pavan',True]
print(f)
f[0]=5
print(f)


# Tuple (Immutable -- We can not change the values)
g = (1,2,3,'Pavan', False)
print(g)

# Dictonaries  (Key value pairs)
my_dict = {'name': 'Pavan', 'city':'Hyd', 'age':25}
print(my_dict['name'])
print(my_dict['city'])


#Set (Removes the duplicate itesm -- only unique item will be there)

my_set = {1,2,2,3,4,4,5}
print(my_set)

print("=========================HANDSON====================")


x = 5
y = 7

addition = x + y
sub = y - x
mul = x * y
division = y / x

print('Addition is :', addition,'sub is :', sub, 'Mul is :', mul, 'divn is :', division)


# List
my_List = [1,2,3,4,5,'Pavan']
print(my_List)
print(my_List[4])

my_List[0]="Check"
print(my_List)


# tuple
my_tub = (1,2,3,4,5,'Pavan')
print(my_tub)
print(my_tub[3])
#my_tub[4]=7
print(my_tub)


# Dictorinies

person = {'name':'Pavan', 'Age': 23, 'City': 'Hyd'}
print(person)
print(person['name'])
del person['City']

person['education'] = 'MCA'
print(person)


# SET
my_Set = {1,1,1,1,2,3,4,5,55}
print(my_Set)