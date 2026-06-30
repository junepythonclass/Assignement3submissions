#with at least 3 examples, explain all operators, all data types and all loops, giving at least 2 examples for each
    #string
name = "Alice"
greeting = 'Hello, World!'
number = "90210"
print(name,greeting,number)

    #integer  
age = 25
temperature = -5
population = 1000000
print(age,temperature,population)

    #complex
coord = 3 + 5j
z = -1j
vector = complex(2, 4)
print(coord,vector,z)

    #float
price = 19.99
pi = 3.14159
height = 1.85
print(price,pi,height)

    #sequence(list,tuples,dictionary)
fruits = ["apple","banana","orange"]
screenSize = (1920,1080)
capitals = {"Uganda":"Kampala","Kenya":"Nairobi","Tanzania":"Dodoma"}
print(fruits)
print(screenSize)
print(capitals)
    #boolean
is_logged_in = True
has_discount = False
is_greater = 5 > 3  # Evaluates to True

#OPERATORS
# 1. Addition (+), Subtraction (-), Multiplication (*)
total = 10 + 5        # 15
diff = 10 - 5         # 5
product = 10 * 5      # 50

# 2. Division (/), Floor Division (//)
div = 10 / 3          # 3.3333333333333335
floor_div = 10 // 3   # 3 (rounds down to nearest integer)

# 3. Modulus (%), Exponentiation (**)
remainder = 10 % 3    # 1
power = 2 ** 3        # 8 (2 cubed)

# 1. Standard Assignment (=)
x = 10

# 2. Add and Assign (+=), Subtract and Assign (-=)
x += 5                # x is now 15
x -= 2                # x is now 13

# 3. Multiply (*=), Divide (/=), Modulus (%=) and Assign
x *= 2                # x is now 26
x /= 2                # x is now 13.0
x %= 5                # x is now 3.0

# 1. Equal (==), Not Equal (!=)
is_equal = (5 == 5)   # True
is_not_equal = (5 != 3) # True

# 2. Greater Than (>), Less Than (<)
g_than = (10 > 5)     # True
l_than = (3 < 1)      # False

# 3. Greater Than or Equal (>=), Less Than or Equal (<=)
g_or_equal = (5 >= 5) # True
l_or_equal = (4 <= 2) # False



#LOOPS
for x in range (1,6):
    if x == 3:
        continue #to skip over an iteration we use continue
    else:
        print(x)

for x in range (1,6):
    if x == 5:
        break #to stop/break the loop
    else:
        print(x)

integer = [10,20,30,40,50]
fruits = ["sugarcane","pineapple","mango","grapes"]
for fruit in fruits:
    if fruit == "pineapple":
        print("Pineapple is sweet")
        break

