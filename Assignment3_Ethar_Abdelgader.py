# A.Data types is used to tells the computer what kind of value you are storing in a variable. 
# The most common data types are integers, floats, strings, lists, and booleans.


# 1. Integers are the whole numbers 
age = 20
students = 35
# here 20 and 35 are integers because they are whole numbers without any decimal points.

# 2. Floats are the decimal numbers 
height = 1.75
price = 15.99
# here 1.75 and 15.99 are floats because they have decimal points.

# 3. Strings are the text values that are inside quotation marks.
name = "Ethar"
city = "Khartoum"
# here "Ethar" and "Khartoum" are strings because they are enclosed in quotation marks.

# 4. Lists are the ordered collections of items 
fruits = ["apple", "banana", "orange"]
# here ["apple", "banana", "orange"] is a list because it is enclosed in square brackets.

# 5. Booleans are the True or False values 
is_student = True
is_teacher = False
# here True and False are booleans because they represent the truth values.



# B. Operators are symbols that tell the computer to perform specific mathematical or logical actions on values.
# 1. Arithmetic operators are used to perform mathematical operations on numbers.

# Operator	           Meaning	               Example
#    +	               Addition	               5 + 3 = 8
#    -	               Subtraction	           10 - 4 = 6
#    *	               Multiplication	       6 * 2 = 12
#    /                 Division	               8 / 2 = 4
#    %	               Remainder	           10 % 3 = 1
#    **	               Power	               2 ** 3 = 8
#    //	               Floor division	       10 // 3 = 3

a = 8
b = 2

print(a + b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# 2. Comparison operators are used to compare two values and return a boolean value (True or False).
# Operator                Meaning               
#   ==                    Equal to
#   !=	                  Not equal to
#   >	                  Greater than
#   <	                  Less than
#   >=	                  Greater than or equal
#   <=	                  Less than or equal

# Ex.1
print(5 > 3)
print(5 == 3)

# Ex.2
age = 18

print(age >= 18)
print(age < 18)

# 3. Assignment operators are used to assign values to variables and perform operations on them.
# Operator          	Meaning	
#    =	                Assignment
#    +=	                Addition and assignment
#    -=	                Subtraction and assignment
#    *=	                Multiplication and assignment
#    /=	                Division and assignment
#    %=	                Remainder and assignment
#    **=	            Power and assignment
#    //=	            Floor division and assignment 

# Ex.1
age = 18
print(age >= 18)
print(age < 18)

# Ex.2
score = 20
score -= 8
print(score)

# 4. Logical operators are used to combine multiple conditions and return a boolean value (True or False).
# Operator	                Meaning
#    and	                Returns True if both conditions are True
#    or	                    Returns True if at least one condition is True
#    not	                Returns True if the condition is False

# Ex.1
age = 20
print(age > 18 and age < 30)

# Ex.2
name = "Ethar"
print(name == "Ethar" or name == "Ahmed")



# D. Conditions help the computer to make decisions based on certain criteria.
# 1. If statement is used to execute a block of code if a certain condition is True.
# Ex.1
age = 20
if age >= 18:
    print("You can vote.")

# Ex.2
marks = 80
if marks >= 50:
    print("Pass")


# 2. If-else statement is used to execute one block of code if a certain condition is True, and another block of code if the condition is False.
# Ex.1
age = 15
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# Ex.2
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. If-elif-else statement is used to execute one block of code if a certain condition is True, another block of code if another condition is True, and a final block of code if none of the conditions are True.
# Ex.1
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# Ex.2
temperature = 35
if temperature > 40:
    print("Very Hot")
elif temperature > 30:
    print("Hot")
else:
    print("Cool")



# E. Loops are used to repeat a block of code multiple times until a certain condition is met.
# 1. For loop is used when you have many items to repeat.
# Ex.1
for i in range(5):
    print(i)

# Ex.2
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(fruit)

# 2. While loop is used when you want to repeat a block of code until a certain condition is False.
# Ex.1
count = 1
while count <= 3:
    print(count)
    count += 1

# Ex.2
number = 5
while number > 0:
    print(number)
    number -= 1