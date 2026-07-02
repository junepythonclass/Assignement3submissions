#1. Data Types
#A data type tells Python what kind of information is being stored.

#1. Integer (int)
#Definition: An integer is a whole number. It has no decimal point.

#Examples:
age = 20
students = 35
temperature = -5

#2. Float (float)
#Definition: A float is a number with a decimal point.

#Examples:
price = 10.50
height = 1.75
weight = 65.8

#3. String (str)
#Definition: A string is text. Strings are written inside quotation marks.

#Examples:
name = "John"
country = "Uganda"
message = "I love Life"

#4. Boolean (bool)
#Definition: A boolean has only two values: True or False.

#Examples:
student = True
raining = False

#5. List (list)
#Definition: A list stores many items in one variable. Lists can be changed hence mutable. It is written with square brackets

#Examples:
fruits = ["Apple", "Banana", "Orange"]
numbers = [10, 20, 30]

#6. Tuple (tuple)
#Definition: A tuple stores many items, but its values cannot be changed hence immutable. It is written with Parentheses brackets

#Examples:
days = ("Monday", "Tuesday", "Wednesday")
coordinates = (12, 25)

#7. Set (set)
#Definition: A set stores unique values only. It does not allow duplicates when the code is run. It uses curly brackets

#Examples:
colors = {"Red", "Blue", "Green"}
numbers = {1, 2, 3, 4}

#8. Dictionary (dict)
#Definition: A dictionary stores information as (key : value pairs). This means that we give the value it key by which we can easy identify the value in the set. A dictionary is also put in curly brackets.

#Examples:
student = {
    "name": "John",
    "age": 20,
    "location": "Buziga"
}



#2. Operators
#It is a symbol, character or anything in statement that tells a computer what to do with an opperand(value, variable, datah). They tell you do something like road signs.

#Assignment Operators
#Assignment operators store values in variables.

#Example
#Assign (=)
x = 10

#Add and Assign (+=)
x = 10
x += 5
print(x)

#Subtract and Assign (-=)
x = 10
x -= 2
print(x)

#Multiply and Assign (*=)
x = 5
x *= 4
print(x)

#Divide and Assign (/=)
x = 20
x /= 4
print(x)

#Arithmetic Operators
#Arithmetic operators are used to perform mathematical calculations.

#Addition (+)
#Adds two numbers.

#Example:
a = 5
b = 3
print(a + b)

#Subtraction (-)
#Subtracts one number from another.

#Example
a = 10
b = 4
print(a - b)

#Multiplication (*)
#Multiplies two numbers.
a = 6
b = 5
print(a * b)

#Division (/)
#Divides one number by another.
a = 10
b = 2
print(a / b)

#Floor Division (//)
#Divides numbers and removes the decimal. So the remainder is not displayed
a = 10
b = 3
print(a // b)

#Modulus (%)
#Returns the remainder after division.
a = 10
b = 3
print(a % b)

#Exponent (**)
#Raises a number to a power.
print(2 ** 3)

#Comparison Operators
#Comparison operators compare two values.

#Equal To (==)
print(5 == 5)

#Not Equal To (!=)
print(5 != 3)

#Greater Than (>)
print(1 > 5)

#Less Than (<)
print(2 < 6)

#Greater Than or Equal To (>=)
print(10 >= 10)

#Less Than or Equal To (<=)
print(8 <= 6)

#Logical Operators
#Logical operators combine conditions for example and, not and or.

#Example
#Both conditions must be True.
age = 20
print(age > 18 and age < 30)

#Only one condition needs to be True.
print(5 > 10 or 5 < 10)

#Changes True to False and False to True.
print(not True)

#Membership Operators
#Checks if something exists for example in.

#Example
fruits = ["Apple", "Banana", "Orange"]
print("Apple" in fruits)

#Checks if something does not exist.
print("Mango" not in fruits)

#Identity Operators
#Checks if two variables refer to the same object for example is.

#Example
a = [1, 2]
b = a
print(a is b)

#Checks if two variables are not the same object.
a = [1, 2]
b = [1, 2]
print(a is not b)


#3. Conditions
# A Condition statement is a block of code it has more than one statement, it is identified by full colonies and there will be indentation, for example if, else, elif.

#if
#Runs code only if the condition is True.

#Example
age = 18
if age >= 18:
    print("You are an adult.")

# if.. else
#Runs one block if the condition is True and another if it is False.

#Example
age = 15
if age >= 18:
    print("Adult")
else:
    print("Child")

#if...elif...else
#Checks several conditions.

#Example
marks = 75
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


#4. Loops
#Loops repeat code. there are two types

#for Loop
#A for loop repeats code a specific number of times or goes through each item in a collection.


#Example 1:
for i in range(5):
    print(i)

#Example 2:
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print("dragon")

#while Loop
#A while loop repeats as long as the condition is True.

#Example
count = 1
while count <= 5:
    print(count)
    count += 1

#Loop Control Statements
#break
#Stops the loop immediately.

#Example
for number in range(10):
    if number == 5:
        break
    print(number)

#continue
#Skips the current loop and moves to the next one.

for number in range(5):
    if number == 2:
        continue
    print(number)

#pass
#Does nothing. It is used as a placeholder when you plan to write code later.
for number in range(5):
    if number == 2:
        pass
    print(number)









