#1. OPERATORS
#What is an Operator?
#An operator is a symbol that tells the computer what action to perform.
#Think of an operator as a worker.

#Example:
#If you tell someone:
#Add 5 and 3.
#The word add is the action.
#In Python:
5 + 3
#The + is the operator.


#A. Arithmetic Operators
#Used for mathematics.

#  Operator	        Meaning	                    Example
#   +	           Addition	                5 + 3 = 8
#   -	           Subtraction	            10 - 4 = 6
#   *	           Multiplication        	6 * 2 = 12
#   /	            Division	            8 / 2 = 4
#   %	           Remainder	            10 % 3 = 1
#   **	             Power	                2 ** 3 = 8
#   //	          Floor Division	        10 // 3 = 3


#Example 1
a = 20
b = 5

print(a + b)

#Output
#25

# Example 2
print(15 % 4)

#Output
#3


#B. Comparison Operators
##These compare two values.

        #They always return:
#True
#or
#False

#Operator	Meaning
#==	        Equal to
#!=	        Not equal
#>	        Greater than
#<	        Less than
#>=	        Greater or equal
#<=	        Less or equalB. Comparison Operators

#These compare two values.
#They always return:

#Example 1
print(20 > 10)

#Output
#True

#Example 2
print(5 == 8)

#Output
#False



#C. Logical Operators
##Used to combine conditions.

#Operator	  Meaning
#and	      Both conditions must be true
#or	          At least one is true
#not	      Opposite

#Example 1
age = 20

print(age > 18 and age < 30)

#Output

#True
#Example 2
print(not False)
#Output
#True


#D.Assignment Operators
#Used to give values to variables.

#Operator	Example
#=	        x = 10
#+=	        x += 5
#-=	        x -= 2
#*=	        x *= 3
#/=	        x /= 2

#Example 1
x = 10
x += 5

print(x)

#Output
#15

#Example 2
marks = 50
marks -= 10

print(marks)
#Output
#40


#2. DATA TYPES
#What is a Data Type?
#A data type tells Python what kind of information you are storing.
#Think of it as different kinds of containers.

#A. Integer (int)
#Whole numbers.
#Examples
age = 19
cars = 25

#B. Float
#Numbers with decimals.
#Examples
height = 5.8
price = 12.50

#C. String (str)
#Words or letters inside quotation marks.
#Examples
name = "John"
country = "Uganda"


#D. Boolean (bool)
#Only two answers.
#True
#False
#Examples
is_student = True
engine_running = False


#E. List
#Stores many items.
#Examples
cars = ["Toyota", "BMW", "Mercedes"]
numbers = [2,4,6,8]



#3. CONDITIONS
#What is a Condition?
#A condition helps a computer make a decision.
#Real life:
#If it rains
#Take an umbrella.
#If not
#Go without one.
#Python does the same.


#A. if Statement
#Example 1
age = 18
if age >= 18:
    print("Adult")


#Example 2
marks = 70
if marks >= 50:
    print("Pass")



#B. if...else
#Example 1
age = 12
if age >= 18:
    print("Adult")
else:
    print("Child")



#Example 2
password = "1234"
if password == "1234":
    print("Access Granted")
else:
    print("Wrong Password")




#C. if...elif...else
#Example 1
marks = 85
if marks >= 80:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

else:
    print("Grade C")


#Example 2
day = "Sunday"
if day == "Monday":
    print("School")

elif day == "Sunday":
    print("Church")

else:
    print("Home")




#4. LOOPS
#What is a Loop?
#A loop repeats something many times.
#Imagine a teacher saying:
#Write your name 10 times.
#Instead of writing it again and again, Python can repeat it automatically.

#A. for Loop
#Used when you know how many times something should repeat.
#Example 1
for i in range(5):
    print("Hello")

#Output
#Hello
#Hello
#Hello
#Hello
#Hello

#Example 2
cars = ["Toyota","BMW","Audi"]
for car in cars:
    print(car)
#Output
#Toyota
#BMW
#Audi


#B. while Loop
#Repeats while a condition is true.
#Example 1
number = 1
while number <= 5:
    print(number)
    number += 1
#Output
#1
#2
#3
#4
#5


#Example 2
fuel = 3
while fuel > 0:
    print("Vehicle Moving")
    fuel -= 1
#Output
#Vehicle Moving
#Vehicle Moving
#Vehicle Moving


#Operators →   Do the work (add, subtract, compare).
#Data Types →  Tell the computer what kind of data it is.
#Conditions →  Help the computer make decisions.
#Loops →       Repeat work automatically.