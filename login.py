
from tkinter import Button, Entry, Label
import tkinter
m=tkinter.Tk()
#insert program
from pymongo import MongoClient
Client=MongoClient("localhost:27017")
db=Client.EmployeeData

# Label(
#               text="Vivek k patel", 
  
#               # Changing font-size here 
#               font=("Arial", 25) ,height=50,width=50,
#               ).pack() 

# button=tkinter.Button(m,text='stop',width=25,command=m.destroy)
# button.pack()
m.geometry('350x200')
lbl = Label(m, text = "Are you a Geek?")
lbl.grid()
txt = Entry(m, width=10)
txt.grid(column =1, row =0)
def clicked():      
    lbl.configure(text = "I just got clicked")
btn = Button(m, text = "Click me" ,
             fg = "red", command=clicked)
btn.grid(column=2, row=0)

# def insert():
#     try:
        
       
#         while True:
#             print('''
#               choices the option
#               1.insert
#               2.show record
#               3.exit
#               ''')
#             op=int(input("select option (1 to 3)"))
#             if op==1:
#                     print("Enter the details")
#                     employeeID=input("Enter the id:-")
#                     employyeName=input("Enter Employee Name:-")
#                     employeeAge=input("Enter Employee Age:-")
#                     employeeCity=input("Enter Employee City:-")
#                     db.employee.insert_one({
#                         "id":employeeID,
#                         "name":employyeName,
#                         "age":employeeAge,
#                         "city":employeeCity,
                        
#                     })
#                     print("Data inserted successfully")
#             elif op==2:
#                     val=db.employee.find_one({'name':'vivek '})
#                     print(val)
#                     print("record is show")
#             elif op==3:
#                  break
#             else:
#                 break
#     except Exception:
#            print(str(e))
         
# insert()
m.mainloop()




--------------------------
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
        
