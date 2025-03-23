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

# age = int(input("How old are you?"))


# if age >100:
#         print("YOU are a century old:")
# elif age >= 18:
#         print("You are an adult:")
# elif age< 0:
#         print("You havaen't been born yet:")
# else:
#         print("You are a child")



# =================================================
# logica; operators(and,or,not) =used to check if two or more conditional statement

# temp =int(input("What is the tmperature outside?:"))
# if  not (temp >=0 and temp<=30):
#        print("the temperature is good today!")
# elif not (temp< 0 or temp >30):
#         print("the temeraure is bad today!")
#         print("stay inside!")
        
        
# ==================================================
# while loop = a statement that will execute its block of code,
#              as long as it's conditon remains true

# name=""

# while len(name) == 0:
#         name = input("Enter your name")
# print("HELLO "+name)

# name=None

# while not name:
#         name = input("Enter your name")
# print("HELLO "+name)


# ============================================
# for loop=a statement that will execute it's block of code 
#          a limited amount of TimeoutError
          
#           while loop = unimited
#           for loop=limited

# for i in range(10):
#         print(i+1)

# for i in range(50,100+1,2):
#         print(i)

# for i in "Vivek k patel":
#         print(i)

# import time
# for second in range(10,0,-1):
#         print(second)
#         time.sleep(1)
# print("HAPPY BIRTHDAY")




# ================================================
# nested loops =The "inner loop" will finish all of it's iterations before 
#                finishing one iteration of the "outer loop"

# rows =int(input("How many rows?"))
# column =int(input("How many column?"))
# symbol=input("Enter a symbol to use:")

# for i in range(rows):
#         for j in range(column):
#                 print(symbol, end=" ")
                
#         print()


# =====================================================================
# Loop Control Statement = change a loops execution from its normal sequence

# break = used to terminate the Loop
# continue =skips to the next iteration of the Loop
# pass = does nothing acts  as a placeholder

# while True:
#         name=input("Enter your name:")
#         if name != "":
#                 break

# continue
# phone_number = "123- 456- 789"
# for i in phone_number:
#         if  i=="-":
#                 continue
#         print(i,end="")

# pass
# for i in range(1,21):
#         if i == 13:
#                 pass
#         else:
#                 print(i)
                
                
# ==============================================
# list =used to store multiple items  in a single variable

# food =["Pizza","humburger","hotdogs","spaghetti"]

# food[0]="shushi"

# print(food)#print list

# print(food[1])#index wise acces element

# food.remove("hotdogs") #remove particluar element
# food.pop() #remove last element
# food.insert(1,"cake") #index stor the element
# food.clear() #clear the list
# for x in food:
#         print(x)



# ===================================================
# 2d list = alist of list

# drink=["Coffie","soda","tea"]
# dinner=["pizza","hamburger","hotdog"]
# dessert=["cake","ice cream"]

# food =[drink,dinner,dessert]

# print(food[0][1])

# --------------------------
# tuple = colletion which  is ordered and unchnageable
#         used to group together related data

# student=("Bro",21,"male")

# print(student.count("Count"))
# print(student.index("male"))

# for i in student:
#         print(i)     

# if 21 in student:     
#         print("Bro is here!")

# len(), min(), max(), tuple(), index(), count(), sum(), and sorted()


# =================================
# set = collecttion which is unorderd, unindexed. No duplicate values

# utensils ={"fork","spoon","knife"}
# v2={1,2,3}
# utensils.add("napkin")

# utensils.remove("fork")

# utensils.clear()
# print(utensils)

# v2=utensils.union(v2)

# print(v2.difference(utensils))

# utensils.update(v2)
# for x in utensils:
#         print(x)


# =============================================
# dictionary = A changable, unorderd collection of unque of qnique key:value
#    pairs Fast beacuse they use hasing ,allow us to access a valur quikly

# capitals = {
#         'Usa' :'washington dc',
#         'india':'new delhi',
#         'china':'beijing',
#         'russia':'moscow'
# }

# capitals.update({'germany':'barline'})
# capitals.update({'Usa':'las veges'})

# capitals.pop('russia')

# capitals.clear()

# # print(capitals['Usa'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#         print(key,value)



#============================================
# index operator [] = give access to a sequence's element (str,list,tuple)

# name = "bro Code"

# if(name[0].islower()):
#         name=name.capitalize()
        
# first_name=name[0:3].upper()
# last_name=name[4:].lower()
# last_character = name[-1]

# print(last_character )``
# print(name)


# ==============================================
# funtion = a block of code which is executed only when it is called

# def hello(a,b,c):
#         print("hello:"+a+b)
#         print("You are "+str(c)+" year old")
#         print("HAve a nice day")
        
# hello("vivek"," patel",23)


 # ====================================================
# return statement =function send Python value/objects back to the caller.
#    These values/object are knows as the function's return value

# def multiply(number1,number2):
#         result =number1+number2
#         return result

# y=multiply(3,5)
# print(multiply(10,20),y)


# =============================================================
# keyword argument = argument preceded by an identifier when we pass them to a fuction
                #    The order of the arguments does'nt matter, unlike position arguments
                #    python knows the names of the arguments that our function recevies
                
        
# def hello(first,middle,last):
#         print("hello "+first+" "+middle +" last")
        
# hello(last='code',middle='Dude',first="BRo")
        

# ==================================================================
# nested function calls= function calls inside other function callls 
#       innermost function calls are resolve first returned Value
#       is used value is used as argument for the next outer function

# num=input("Enter a whole postivie number:")
# num =float(num)
# num=abs(num)
# num=round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number:")))))



# ======================================================================
# Scope =The region that a variable is recognized
#       A varible is only availabe from inside the region it is create
#       A global and locally scoped version a variable can be created.
      
# name = "Bro" #Global scope (availble inside & outside functions)

# def display_name():
#         name="Code"
#         print(name)
        
# display_name()        
# print(name)



# =========================================================================
# args = paramater that will pack all agrument into a tuple
#        useful so that a function can accept a varying amount of argument
   
       
# def add(*args): # args /stuff
#         sum=0
#         for i in args:
#                 sum += i
#         return sum

# print(add(1,2,3,4,5))


# ==========================================================================
# **kwargs = parameter that will pack all arguments into a dictionary
#           useful so that a function can accept a varying amount of keyword 
#           argument

# def hello(**kwargs):
#         print("HEllo"+kwargs['first']+" "+kwargs['last'])
#         print("HEllo",end=" ")
        
#         for key,value in kwargs.items():
#                 print(value,end="")
                
        
# hello(title="Mr.",first="Bro",middle="Dude",last="Code")



# =========================================================================
# str.format = optional method that gives users more control when displaying output


# animal ="cow"
# item ="moon"


# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item))
# print("The {item} jumped over the {animal}".format(animal="cow123",item="moon"))

# text = "The {} jumped over the {}"
# print(text.format("vivek","PAtel"))


# =========================================================
# str.format()  = optional method that gives users more
#                control when display output
# number =1000
# print("The number pi is {:.3f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))



# ==========================================================
# import random

# x= random.randint(1,6)
# y=random.random()

# myList = ['rock','paper','scissors']
# z = random.choice(myList)

# print(z)


# card = [1,2,3,4,5,6,7,8,9,"a","b","c"]

# random.shuffle(card)

# print(card)


# =============================================
# exception= events detected during execution that interupt the flow of a program

# try:
#    numerator = int(input("Enter a number to divide:"))
#    demoninator = int(input("Enter a number to divide by:"))
#    result=numerator/demoninator
#    print(result)
# except ZeroDivisionError as e:
#    print(e)
#    print("You can't divide by zero! idiot")
# except ValueError as e:
#    print(e)
#    print("Enter only number plz")
# except Exception as e:
#     print(e)
#     print("Something went wrong:(")



# =========================================================
# import os

# path="G:\\python\\first python\\python_doc\\python_doc\\new.txt"

# if os.exists(path):
#         print("That location doesn't!")
#         if os.path.isfile(path):
#                 print("That is a file")
#         elif os.path.isdir(path):
#                 print("That is a directory!")
# else:
#         print("That location doesn't exist")



# ============================================================
# open the file

# try:
#    with open('python_doc\\new.txt') as file:
#         print(file.read())
        
  
# except FileNotFoundError:
#    print("That file was not found:")      
# print(file.closed)


# ============================================================
#already file in add content

# text ="Have a good nice day! see ya:\n"

# with open('python_doc\\new.txt','w') as file:
#         file.write(text)
        
        
# ==============================================================
# copyfile()= copies contents of a File
# copy()= copyfile() + permission mode + destination can be a direcory
# copy2()= copy() + copies metadata(file's creation and modification times)

# import shutil

# shutil.copyfile('python_doc\\new.txt','python_doc\copy.txt')



# ============================================================
# moved the file


# import os

# source="python_doc\\copy.txt"
# destination="python_doc\\leacture\\copy.txt"

# try:
#    if os.path.exists(destination):
#            print("There is already a file there")
#    else:
#            os.replace(source,destination)
#            print(source+"Was moved")
# except FileNotFoundError:
#         print(source+"was not found")


# ===================================================
# delete the file

import os
import shutil

path="python_doc\\leacture\\copy.txt"

try:
     os.remove(path) #delete a file
     os.rmdir(path)   #delete an ematy directory
     shutil.rmtree(path)  #delete a directory cantaining files
except FileNotFoundError:
        print("That file was not found")

except PermissionError:
        print("You do not have permission to delete that")
except OSError:
        print("You cannot delte that using that function")
        
else:
        print(path+"was deleted")