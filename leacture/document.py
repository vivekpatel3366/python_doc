# Python #

# python is supported with linux, mac os, windows 

# python supports various database engine like mysql, pgsql, mongodb , mysqli, sqlite 

# Python is a pouplar for it's easy to use syntax 

# Python has builtin framworks avaliable like Django and Flask \

# For windows you can use both command py and python


# Print 
# print('Hello ! python')

# Python Variables

a = '1223'

# Variable declaration rules

# 1. Alphanumeric combinatio can be used to decalre variable. 

a1 = '123'

# 2. Variable should always start with any albhabet or underscore

# 3. Variables are case sensitive 

b = 'abc'
B = 'xyz'

# 4. Reserved Keywords of python can not be used as variables

#for = 'loop'

# Data types 
 # 1. Strig 'str'

str1 = 'string value'
str1= 'vivek patel'
#print(str)
#print(type(str))


 # 2. Numeric types 

        # 2.1 - integer 
num = 123
num1 = '123'
num2 =233

print(type(num))
print(type(num1))




        # 2.2 - float
numf = 2.3 
numf2=3.5
print(type(numf))        
        # 2.3 - complex 
cnum = 2+3j 
cnum1=4+5j
print(type(cnum))        

# 3. Sequence type 
        # 3.1 - list
        # 3.2 - tuple
        # 3.3 - range

# 4. Mapping type - Dict (Dictionary 
# 5. Boolean type - True , False 
# 6. Set 
# 7. None 


# -------------------------------------------------
# integer
# age = 21
# print("vivek k patel :"+str(age)) 
# print(type(age))
# -----------------------------------------------------

# floating number
# height=72.45
# print("Your height is : "+str(height))
# print(type(height))

    
# ----------------------------------------------------

# boolean 
# human = False
# print("Are you a human : "+str(human))  **
# print(type(human))


# ---------------------------------------------------

# 1 asssignment
# a=b=c=d="vivek"      **

# print(a)
# print(b)
# print(c)
# print(d)


# --------------------------------------------------
# method in python
# name="BRo code"

# print(len(name)) #len

# print(name.find("R")) #find

# print(name.capitalize()) #capitalize

# print(name.upper()) #upper case

# print(name.lower()) #lowe case

# print(name.isdigit()) #isdegit check value

# print(name.isalpha()) #isalfa check in value

# print(name.count('o')) #count the charcter/word

# print(name.replace('o','e')) #replace the value


# =============================================================================
# typeCasting

# x = 1 #int
# y = 2.0 #float
# z = "3" #str

# # integer convert
# x = int(x)
# y = int(y)
# z = int(z)
# print(x,y,z)

# # float convert
# x = float(x)
# y = float(y)
# z = float(z)
# print(x,y,z)


# # String convert
# x = str(x)
# y = str(y)
# z = str(z)
# print(type(x),y,z)


# #comlex convert
# x = complex(x)
# y = complex(y)
# z = complex(z)
# print(type(x),y,z)

# ======================================================
# input the user
# name =input("What is your name : ")
# age = int(input("How old are you ?"))
# height =float(input("How tall are you?"))


# print('Hello ' + name)
# print("You are "+str(age)+" year old")
# print("You are "+str(height)+" cm tall")



# =================================================
# import mat libary
# import math
 
# pi = 3.14

# print(round(pi)) #round

# print(math.ceil(pi)) #ceil

# print(math.floor(pi)) #floor

# print(abs(pi)) #abs

# print(pow(pi,3)) #power

# print(math.sqrt(49)) #sqrt

# print(max(10,20,30)) #maximum value

# print(min(10,20,30)) #minmum value



# ==================================================
#slicing = create a substirn by extracting elements from another string index[] or slice()
#   [start:stop:step]

# name ="Bro Code" 

# first_name=name[0:3]
# last_name=name[4:]
# funky_name=name[0:8:2]
# reverse_name=name[::-1]

# print(reverse_name)

# website="vivek kanubhai patel"
# website2="hello friends good morning"
# slice =slice(10,-6) #object in slice
# print(website[slice])
# print(website2[slice])


# ================================================
# if statement = ablock of code that will extcute it's conditio is true

age = int(input("How old are you?"))

if age >= 18:
        print("You are an adult:")
elif age< 0:
        print("You havaen't been born yet:")
else:
        print("You are a child")