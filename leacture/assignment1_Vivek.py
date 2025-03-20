# print("hello")
# list=[10,30,2,4,5,5,2,3]
# list2=[]


# def append1():
#     n=int(input("Enter the only number value - "))
#     list.append(n)
#     # print(list)

# def clear1():
#     list.clear()
#     # print(list)
    
# def copy12():
#     l1=[12,30,100,200]
#     print("old list",l1)
#     l1=list.copy()
#     print("copy list1 --",l1)
    
# def count12():
#     a=int(input("enter the number - "))
#     c1=list.count(a)
#     print("count element = ",c1)
    
# def extend12(): 
#     b=input("Enter the character/word - ")
#     list2.append(b)
#     list.extend(list2)    
#     # print(list)

# def index12():
#     c=int(input("enter the only in list available number value - "))
#     index1=list.index(c)
#     print(index1)
    
# def insert12():
#     d=int(input("in which index you want to add element - "))
#     e=int(input("Enter the element - "))
#     a1=list.insert(d,e)
#     print(a1)
    
# def pop12():
#     a2=list.pop()
#     print(a2)
#     # print(list)
    
# def remove123():
#     f=int(input("Enter the remove element - "))
#     list.remove(f)
#     print("Remove the element- ",f)
    
# def revese12():
#     list.reverse()
#     print("reverse list- ",list)
    
    
    
# while True:
#     print(list)
#     print("""
#           -Enter the choices 
#           1).append the element
#           2).clear the list
#           3).copy one list to second list
#           4).list the count element
#           5).extends the list
#           6).index wise show value
#           7).insert the element
#           8).pop the element
#           9).remove element
#           10).reverse the list
#           11).exit the program
          
#           """)
#     num=int(input("Enter the choice number :==> "))
#     print("\n")
    
#     if num == 1:
#         append1()
#     elif num == 2:
#         clear1()
#     elif num == 3:
#         copy12()
#     elif num == 4:
#         count12()
#     elif num == 5:
#         extend12()
#     elif num == 6:
#         index12()
#     elif num == 7:
#         insert12()
#     elif num == 8:
#         pop12()
#     elif num == 9:
#         remove123()
#     elif num == 10:
#         revese12()
#     elif num == 11:
#         break
       
 
 
 
 
 
 
Vlist=[10,30,50,70,40,60,50]      
def listshow():
    print("Original list :",Vlist)

def listappend1():
    Vlist.append(12)
    print("After append : ",Vlist)
    
def listcopy1():
    Vlist1=Vlist.copy()
    print("After copy : ",Vlist1)

def listcount1():
    v=Vlist.count(50)
    print("count the element : ",v)

def listextend1():
    a=['vivek','raj','manish']
    Vlist.extend(a)
    print("After extend : ",Vlist)

def index1():
    index1=Vlist.index(50)
    print("After index : ",index1)

def insert1():
    Vlist.insert(3,90)
    print("After insert : ",Vlist)

def pop1():
    Vlist.pop()
    print("After pop : ",Vlist)

def remove1():
    Vlist.remove(30)
    print("After remove :",Vlist)

def reverse1():
    Vlist.reverse()
    print("After reverse : ",Vlist)

def clear1():
    Vlist.clear()
    print("after clear : ",Vlist)


listshow()
listappend1()
listcopy1()
listcount1()
listextend1()
index1()
insert1()
pop1()
remove1()
reverse1()
clear1()