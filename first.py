#---------------Python---------------------------
# The import statement
import datetime

# Multi-Line Statements
addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70
print(addition)

# The pass statement
def fun1(arg):
    pass

# The del statement
del addition

# The return statement  
def addtion():
    return 10+20

# ---------------------------------------------

# Break Statement in Python
number=[10,20,30,40,]
for i in number:
    if i>30:
        break
    print('current number ',i)
    
#    Break while loop
name= 'vivek k patel'
size =len(name)
i=0
while i<size:
    if name[i].isspace():
        break
    print(name[i],end='')
    i=i+1

# Break Nested Loop in Python
for i  in range(1,11):
    print("multipication table of",i)
    for j in range(1,11):   
        if i>5 and j>5:
            break
        print(i*j,end=' ')
    print('')
    
    
#---------------------------------------------------------------- 

# Continue Statement in Python
for i in range(1,11):
    if(i==5):       
        continue
    print(i)
    
# Pass Statement in Python
months = ['January', 'June', 'March', 'April']
for mon in months:
    pass


# ------------------------------------------------------------------

# Python Keywords
# Get the List of Keywrods
import keyword
print(keyword.kwlist)


# -----------------------------------------------------
# Types of Keywords
# Value Keywords: True, False, None.    
# Operator Keywords: and, or, not, in, is
# Conditional Keywords: if, elif, else
# Iterative and Transfer Keywords: for, while, break, continue, else
# Structure Keywords: def, class, with, as, pass, lambda
# Import Keywords: import, from, as
# Returning Keywords: return, yield
# Variable Handling Keywords: del, global, nonlocal
# Returning Keywords: return, yield
# Asynchronous Programming Keywords: async, await
# -------------------------------------------------

# ---------------------------------------------------------
# Python Operators

# 1)Arithmetic operator
    # + (Addition)
    # - (Subtraction)
    # * (Multiplication)
    # / (Division)
    # // Floor division)
    # ℅ (Modulus)
    # ** (Exponentiation)
# ----------------------------
#2)Relational (comparison) operators
x = 10
y = 5
z = 2

# > Greater than
print(x > y)  # True
print(x > y > z)  # True

# < Less than
print(x < y)  # False
print(y < x)  # True

# Equal to 
print(x == y)  # False 
print(x == 10)  # True 

# != Not Equal to 
print(x != y)  # True 
print(10 != x)  # False 

# >= Greater than equal to
print(x >= y)  # True
print(10 >= x)  # True

# <= Less than equal to
print(x <= y)  # False
print(10 <= x)  # True


# -------------------------------------
# Logical operators
a = 2
b = 4

# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")

# ----------------------------------
# or (Logical or)
a = 2
b = 4

if a > 0 or b < 0:
    # at least one expression is true so conditions is true
    print(a + b)  # 6
else:
    print("Do nothing")
    
# ---------------------------------
# not (Logical not)

a = True

# Logical not
if not a:
    # a is True so expression is False
    print(a) 
else:
    print("Do nothing")
    
# -------------------------------
#  in operator
my_list = [11, 15, 21, 29, 50, 70]
number = 15
if number in my_list:
    print("number is present")
else:
    print("number is not present")
    
# Not in operator
my_tuple = (11, 15, 21, 29, 50, 70)
number = 35
if number not in my_tuple:  
    print("number is not present")
else:
    print("number is present")
    
# -----------------------------------   
# is operator
x = 10          
y = 11 
z = 10
print(x is y)
print(x is z) 

# -----------------------------------
# is not operator
x = 10
y = 11 
z = 10
print(x is not y)
print(x is not z) 


# -------------------------------------------------------------
# Bitwise Operators
# Bitwise and &
a = 7
b = 4
c = 5
print(a & b)
print(a & c)
print(b & c)

# Bitwise or |
a = 7
b = 4
c = 5
print(a | b)
print(a | c)
print(b | c)

# Bitwise xor ^
a = 7
b = 4
c = 5
print(a ^ c)
print(b ^ c)

# -------------------------------------------------------------------------------
# Python Variables
# -------------------------------------------------------------------------------
# Creating a variable
name = "John"  # string assignment
age = 25  # integer assignment
salary = 25800.60  # float assignment

print(name)  # John
print(age)  # 25
print(salary) 


# Changing the value of a variable
var = 10
print(var)  # 10
# print its type
print(type(var))  # <class 'int'>

# assign different integer value to var
var = 55
print(var)

# Integer variable  
age = 28


# Float variable
salary = 10800.55

# Complex type
a = 3 + 5j


# ----------------------------------------------------------------------------
# List type variable
# create list
my_list = ['Jessa', 10, 20, 'Kelly', 50, 10.5]
# print entire list
print(my_list)  # ['Jessa', 10, 20, 'Kelly', 50, 10.5]

# Accessing 1st element of a list
print(my_list[0])  # 'Jessa'

# Accessing  last element of a
print(my_list[-1])  # 10.5

# access chunks of list data
print(my_list[1:3])  # [10, 20]

# Modifying first element of a list
my_list[0] = 'Emma'
print(my_list[0])  # 'Emma'

# add one more elements to list
my_list.append(100)
print(my_list)  # ['Emma', 10, 20, 'Kelly', 50, 10.5, 100]



# --------------------------------------------------------------------------
# Get the data type of variable

a = 100
print(type(a))  # class 'int'

b = 100.568
print(type(b))  # class 'float'

str1 = "PYnative"
print(type(str1))  # class 'str'

my_list = [10, 20, 20.5, 100]
print(type(my_list))  # class 'list'

my_set = {'Emma', 'Jessa', 'Kelly'}
print(type(my_set))  # class 'set'

my_tuple = (5, 10, 15, 20, 25)
print(type(my_tuple))  # class 'tuple'

my_dict = {1: 'William', 2: 'John'}
print(type(my_dict))  # class 'dict'

# ----------------------------------------------------------------
# Local variable
# def test1():  # defining 1st function
#     price = 900  # local variable
#     print("Value of price in test1 function :", price)

# def test2():  # defining 2nd function
#     # NameError: name 'price' is not defined
#     print("Value price in test2 function:", price)

# # call functions
# test1()
# test2()


# Global variable
# price = 900  # Global variable

# def test1():  # defining 1st function
#     print("price in 1st function :", price)  # 900

# def test2():  # defining 2nd function
#     print("price in 2nd function :", price)  # 900

# # call functions
# test1()
# test2()


# ===============================================================================
# Python Casting: Type Conversion and Type Casting

'''
Implicit casting: The Python interpreter automatically performs an implicit Type conversion, which avoids loss of data.
Explicit casting: The explicit type conversion is performed by the user using built-in functions
'''

# Casting float value to an integer

pi = 3.14  # float number
print(type(pi))
# Output class 'float'

# converting float integer
num = int(pi)
print("Integer number:", num)
# Output  3
print(type(num))

# --------------------------------------------------------------------  
# Casting Boolean value to an integer

flag_true = True
flag_false = False
print(type(flag_true))
# Output class 'bool'

# converting boolean to integer
num1 = int(flag_true)
num2 = int(flag_false)

print("Integer number 1:", num1)  
# Output 1
print(type(num1))  
# Output class 'int'

print("Integer number 2:", num2)
# 0
print(type(num2))

# --------------------------------------------------------------
# Casting a string to an integer
string_num = "225"
print(type(string_num))
# Output class 'str'

# converting str to integer
num1 = int(string_num)

print("Integer number 1:", num1)
# Output 225
print(type(num1))

# ------------------------------------------------------------
# Casting integer to float
num = 725
print(type(num))
# Output class 'int'

# converting float to integer
num1 = float(num)

print("Float number:", num1)
# Output 725.0
print(type(num1))

# --------------------------------------------------------

# Casting Boolean to float
flag_true = True
flag_false = False
print(type(flag_true)) 
# Output class 'bool'

# converting boolean to float
num1 = float(flag_true)
num2 = float(flag_false)

print("Float number 1:", num1)
# Output 1.0
print(type(num1))
# class 'float'

print("Float number 2:", num2)
# Output 0.0
print(type(num2))

# ----------------------------------------------------
# Casting string to float
string_num = "725.535"
print(type(string_num))
# Output class 'str'

# converting str to float
num1 = float(string_num)

print("Float number:", num1)
# Output 725.535
print(type(num1))


# --------------------------------------------------------------
# Complex type conversion
# Casting integer type to complex type
r_num = 135
print(type(r_num)) # class 'int'

# converting int to complex(x)
c_num = complex(r_num)

print("Complex number:", c_num)
# Output (135+0j)
print(type(c_num))
# class 'complex'

# converting int to complex(x, y)
r_num, i_num2 = 135, 235
c_num = complex(r_num, i_num2)

print("Complex number:", c_num)
# Output (135+235j)
print(type(c_num)) 



# --------------------------------------------------------------
# Casting float type to complex type
r_num = 53.250
print(type(r_num))  # class 'float'

# converting float to complex(x)
c_num = complex(r_num)

print("Complex number:", c_num)
# Output (53.25+0j)
print(type(c_num))  
# class 'complex'

# converting float to complex(x, y)
r_num, i_num2 = 53.250, 350.750
c_num = complex(r_num, i_num2)

print("Complex number:", c_num)
# Output (53.25+350.75j)
print(type(c_num))


# ------------------------------------------------------------
# Casting Boolean type to complex type
boolean_true = True
print(type(boolean_true))  # class 'bool'

# converting boolean to complex(x)
c_num = complex(boolean_true)

print("Complex number:", c_num)  
# Output (1+0j)
print(type(c_num))
# class 'complex'

# converting boolean to complex(x, y)
r_bool, i_bool = False, True
c_num = complex(r_bool, i_bool)

print("Complex number:", c_num)
# Output 1j
print(type(c_num))

# ----------------------------------------------------------------
# Bool type conversion
# Casting integer to Boolean type
num1 = 10
num2 = 0
print(type(num1))  # class 'int'

# Convert into to bool
b1 = bool(num1)
b2 = bool(num2)

print(b1)
# Output True
print(b2)
# Output False

print(type(b1))

# ------------------------------------------------------------
# Casting float to Boolean type
f_num1 = 25.35
f_num2 = 0.0
print(type(f_num1))  # class 'float'

# Convert float into to bool
b1 = bool(f_num1)
b2 = bool(f_num2)

print(b1)
# Output True

print(b2)
# Output False

print(type(b1))

# ------------------------------------------------------------
# Casting string to Boolean type
s1 = "False"
s2 = "True"
s3 = "812"
s4 = ""
print(type(s1))  # class 'str'

# Convert string into to bool
b1 = bool(s1)
b2 = bool(s2)
b3 = bool(s3)
b4 = bool(s4)

print(b1)  # True
print(b2)  # True
print(b3)  # True
print(b4)  # False
print(type(b1))

# -----------------------------------------------------------
# Casting complex type to Boolean type
c1 = 33 + 9j
c2 = 0 + 0j
print(type(c1))  # class 'complex'

# Convert complex value into to bool
b1 = bool(c1)
b2 = bool(c2)

print(b1)  # True
print(b2)  # False
print(type(b1))

# -----------------------------------------------------------
# String type conversion

# Casting int to str type
num = 15
print(type(num))  # class 'int'

# converting int to str type
s1 = str(num)
print(s1)
# Output '15'
print(type(s1))

# ----------------------------------------------------
# Casting float type to str type
num = 75.35
print(type(num))  # class 'float'

# converting float to str type
s1 = str(num)
print(s1)
# Output '75.35'
print(type(s1))

# --------------------------------------------------
# Casting complex type to str  type
complex_num = 15 + 5j
print(type(complex_num))  # class 'complex'

# converting complex to str type
s1 = str(complex_num)
print(s1)
# Output '(15+5j)'

print(type(s1))

# --------------------------------------------------
# Casting bool type to str type
b1 = True
b2 = False
print(type(b1))  # class 'bool'

# converting bool to str type
s1 = str(b1)
s2 = str(b2)
print(s1)
# Output 'True'
print(s2)
# Output 'False'
print(type(s1))

# ===========================================================
# Python Input: Take Input from User
# Python Example to Accept Input From a User


name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

# Display all values on screen
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)


# ----------------------------------------
# Take an Integer Number as input from User
first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))

print("\n")
print("First Number:", first_number)
print("Second Number:", second_number)
sum1 = first_number + second_number
print("Addition of two number is: ", sum1)

# -----------------------------------------
# Take Float Number as a Input from User
marks = float(input("Enter marks "))
print("\n")
print("Student marks is: ", marks)
print("type is:", type(marks))


# ---------------------------------------
# Get Multiple inputs From a User in One Line
name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()
print("\n")
print("User Details: ", name, age, marks)


# ---------------------------------------
# Accept Multiline input From a User
data = []
print("Tell me about yourself")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
finalText = '\n'.join(data)
print("\n")
print("Final text input")
print(finalText)


# --------------------------------------
# Python Input() vs raw_input()
# name = raw_input("Enter your name ")
# print ("Student Name is: ", name)
# print (type(name))

# age = raw_input("Enter your age ")
# print ("Student age is: ", age)
# print (type(age))


# ------------------------------------------
# Display Output Number in Various Format
number = int(input("Enter number "))

print("\n")
# 'd' is for integer number formatting
print("The number is:{:d}".format(number))

# 'o' is for octal number formatting, binary and hexadecimal format
print('Output number in octal format : {0:o}'.format(number))

# 'b' is for binary number formatting
print('Output number in binary format: {0:b}'.format(number))

# 'x' is for hexadecimal format
print('Output number in hexadecimal format: {0:x}'.format(number))

# 'X' is for hexadecimal format
print('Output number in HEXADECIMAL: {0:X}'.format(number))


# ----------------------------------------------
# Output String Alignment
text = input("Enter String ")

print("\n")
print("Left justification", text.ljust(60, "*"))
print("Right justification", text.rjust(60, "*"))
print("Center justification", text.center(60, "*"))