
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