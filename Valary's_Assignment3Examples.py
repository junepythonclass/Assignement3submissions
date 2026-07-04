#with at least 3 examples, explain all operators, all data types and all loops, giving at least 2 examples for each
    #string
name = "Emma"
greeting = 'Hello, Mr'
year = 1986
print(greeting,name,"of",year)

    #integer  
age = 25
shoe_size = 42
children = 5
print(age,shoe_size,children)

    #complex
coord = 9 + 6j
z = -1j
vector = complex(8, 14)
print(coord,vector,z)

    #float
price = 55.3
pi = 3.14159
height = 5
print(price,pi,height)

    #sequence(list,tuples,dictionary)
fruits = ["grapes","dates","oranges"]
screenSize = (1947,1740)
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
total = 14 + 5        # 19
diff = 15 - 5         # 10
product = 5 * 5      # 25

# 2. Division (/), Floor Division (//)
div = 10 / 3          # 3.3333333333333335
floor_div = 10 // 3   # 3 (rounds down to nearest integer)

# 3. Modulus (%), Exponentiation (**)
remainder = 10 % 3    # 1
power = 2 ** 3        # 8 (2 cubed)

# 1. Standard Assignment (=)
x = 5

# 2. Add and Assign (+=), Subtract and Assign (-=)
x += 6                # x is now 11
x -= 3                # x is now 9

# 3. Multiply (*=), Divide (/=), Modulus (%=) and Assign
x *= 2                # x is now 18
x /= 2                # x is now 9.0
x %= 3                # x is now 3.0

# 1. Equal (==), Not Equal (!=)
is_equal = (7 == 7)   # True
is_not_equal = (8 != 3) # True

# 2. Greater Than (>), Less Than (<)
g_than = (20 > 1)     # True
l_than = (8 < 5)      # False

# 3. Greater Than or Equal (>=), Less Than or Equal (<=)
g_or_equal = (2 >= 2) # True
l_or_equal = (7 <= 2) # False



#LOOPS
for x in range (1,7):
    if x == 4:
        continue #to skip over an iteration we use continue
    else:
        print(x)

for x in range (1,7):
    if x == 6:
        break #to stop/break the loop
    else:
        print(x)

integer = [5,10,15,80,90]
fruits = ["cherry","apple","kiwi","grapes"]
for fruit in fruits:
    if fruit == "kiwi":
        print("kiwi is sweet")
        break