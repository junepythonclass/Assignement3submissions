# PYTHON DATA TYPES

# 1. String; Text which is enclosed in quotes
name = "Pimer"
position = 'Software Engineer'

#Numeric; Numbers
# 2. Integer; Whole numbers
age = 23
height = 162

# 3. Float; Decimal numbers
weight = 59.90 
marks = 85.5

#Sequence; Ordered collection of items
# 5. List; These can be changed
fruits = ["Apple", "Banana", "Mango"]
car = ["Toyota", "Honda", "Ford"]

# 6. Tuple; These cannot be changed
colors = ("Red", "Blue", "Green")
utensils = ("Spoon", "Fork", "Knife")

# 8. Boolean; True or False
is_student = True
is_employed = False

# 9. Set; Unique values only
numbers = {1, 2, 2, 3}
girl_friends = {"Pimer", "Mercy", "Scholastica"}



# OPERATORS

# ARITHMETIC OPERATORS

# Addition (a + b); 3 + 2 = 5
# Subtraction (a - b); 3 - 2 = 1
# Multiplication (a * b); 3 * 2 = 6
# Division (a / b); 3 / 2 = 1.5
# Floor Division (a // b); 3 // 2 = 1 - rounds to the nearest whole number
# Modulus (a % b); 3 % 2 = 1 - gives the remainder of the division
# Exponent (a ** b); 3 ** 2 = 9

#examples 
a = 10
b = 3

print(a + b)   # Addition; 10 + 3 = 13
print(a - b)   # Subtraction; 10 - 3 = 7
print(a * b)   # Multiplication; 10 * 3 = 30
print(a / b)   # Division; 10 / 3 = 3.333...
print(a // b)  # Floor Division; 10 // 3 = 3
print(a % b)   # Modulus (remainder); 10 % 3 = 1
print(a ** b)  # Exponent (10³); 10 ** 3 = 1000

# ASSIGNMENT OPERATORS

# Assignment operators are used to assign values to variables. 
# The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left. 
# There are also compound assignment operators that combine an arithmetic operation with assignment, such as +=, -=, *=, /=, etc.
# Addition assignment (a += b); a = a + b
# Subtraction assignment (a -= b); a = a - b
# Multiplication assignment (a *= b); a = a * b
# Division assignment (a /= b); a = a / b
# Floor Division assignment (a //= b); a = a // b
# Modulus assignment (a %= b); a = a % b
# Exponent assignment (a **= b); a = a ** b

# Examples
x = 5 # assign 5 to x
x += 2 # add 2 to x, now x is 7

x -= 1 # subtract 1 from x, now x is 6
x *= 2 # multiply x by 2, now x is 12

# COMPARISON OPERATORS

# Comparison operators are used to compare two values. 
# They return a boolean value (True or False) based on the comparison.
# Equal (a == b); True if a is equal to b
# Not Equal (a != b); True if a is not equal to b
# Greater than (a > b); True if a is greater than b
# Less than (a < b); True if a is less than b
# Greater than or Equal (a >= b); True if a is greater than or equal to b
# Less than or Equal (a <= b); True if a is less than or equal to b

# Examples
a = 10
b = 5

print(a == b); #a is equal to b, false 
print(a != b)   # a is not equal to b, true
print(a > b)    # a is greater than b, true
print(a < b)    # a is less than b, false
print(a >= b)   # a is greater than or equal to b, true
print(a <= b)   # a is less than or equal to b, false

# LOGICAL OPERATORS

# Logical operators are used to combine conditional statements.
# and; Returns True if both statements are true
# or; Returns True if one of the statements is true
# not; Returns True if the statement is false

print(True and False)
print(True or False)
print(not True)

# Examples
age = 20
position = "Software Engineer"

if age > 18 and position == "Software Engineer":
    print("Eligible for the job")   # Eligible for the job, which is true because both conditions are true
else:
    print("Not eligible for the job") # Not eligible for the job, which is false because one of the conditions is false


# MEMBERSHIP OPERATORS

# Membership operators are used to test if a sequence (such as a string, list, or tuple) contains a certain value.
# in; Returns True if a sequence contains a certain value
# not in; Returns True if a sequence does not contain a certain value

# Examples
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits) # True, because "Apple" is in the list of fruits
print("Orange" not in fruits) # True, because "Orange" is not in the list of fruits

# IDENTITY OPERATORS

# Identity operators are used to compare the memory locations of two objects.
# is; Returns True if both variables point to the same object in memory
# is not; Returns True if both variables do not point to the same object in memory

# Examples
x = 2
y = 2
z = 3

print(x is y) # True, because x and y point to the same object in memory
print(x is z) # False, because x and z point to different objects in memory
print(x is not z) # True, because x and z point to different objects in memory


# LOOPS

# For Loop
# The for loop is used to run a block of code a certain number of times. 
# It is often used to iterate over a sequence (like a list, tuple, or string).

# Examples
for i in range(5):
    print(i) # this will print numbers from 0 to 4 because range(5) generates numbers from 0 to 4
    # range means a sequence of numbers starting from 0 and ending at the specified number (5 in this case) 
    # but not including that number.

for fruit in fruits:
    print(fruit) # this will print each fruit in the list of fruits, ie, Apple, Banana, Mango as mentioned above


# Continue; this is used to skip a certain iteration in a loop and continue with the next iteration.
for i in range(1, 6):
    if i == 3:
        continue # this will skip the iteration when i is 3 and continue with the next iteration
    print(i)

# Break; This is used to stop the loop when a certain condition is met.
for i in range(1, 6):
    if i == 4:
        break # this will stop the loop when i is 4 and exit the loop
    print(i)

# Loop through a list; this will print each item in the list
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits: # this will loop through each item in the list of fruits and print it, ie, Apple, Banana, Mango
    print(fruit)


# While Loop; this is used to run a block of code as long as a certain condition is true.
count = 1

while count <= 3:
    print(count) # this will print the value of count as long as it is less than or equal to 3, which is 1, 2, 3
    count += 1

# Break in while loop; this is used to stop the loop when a certain condition is met.
num = 5

while num > 0:
    if num == 3:
        break
    print(num) # this will print the value of num as long as it is greater than 0, which is 5, 4, 
    #and then it will break the loop when num is 3
    num -= 1

# Continue in while loop; this is used to skip a certain iteration in a while loop and continue with the next iteration.
step = 0 

while step < 5:
    step += 1
    if step == 3:
        continue
    print(step)
