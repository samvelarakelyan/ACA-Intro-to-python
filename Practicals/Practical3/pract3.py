

"""
LISTS:
------------------------------
"""
#1)
list1=["hello",1,True]
print("list1 beafore adding values:",list1)

elem1=input("Please enter the first element you want to add:")
elem2=input("please enter the second element you want to add:")
elem3=input("please enter the third element you want to add:")

list1.append(elem1)
list1.append(elem2)
list1.append(elem3)

print("list1 after adding values:",list1)
#------------------------------------------------------

#2)
list1=["hello",1,True]
print("list1:",list1)

list1_copy=list1.copy()

elem1=input("Please enter the first element you want to add:")
elem2=input("please enter the second element you want to add:")
elem3=input("please enter the third element you want to add:")

list1_copy.append(elem1)
list1_copy.append(elem2)
list1_copy.append(elem3)

print("list1_copy:",list1_copy)
#------------------------------------------


#3)
list2=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

value=int(input("enter a value from the list2:"))
count=list2.count(value)

print("Number of %ds = %d" %(value,count))
#--------------------------------------------------


#4)
list4=["c","python","c++","java","c#","javascript"]
print("list4 before removeing element:",list4)

value=input("enter a value from the list4:")

list4.remove(value)
print("list4 after removeing element:",list4)
#--------------------------------------------------------


#5)
list5=[5,"python",True,3.14,55,"c++",False,2.7]
print("list5:",list5)

list5.pop(5)
list5.pop(4)
list5.pop(0)

print("list5:",list5)
#--------------------------------------------------------


#6)
list5=[5,"python",True,3.14,55,"c++",False,2.7]
print("list5:",list5)

list5_copy=list5.copy()

list5_copy.pop(5)
list5_copy.pop(4)
list5_copy.pop(0)

print("list5_copy:",list5_copy)
#--------------------------------------------------------


#7)
l1=["python",3.7,True,632]
l2=["Jpython",234,False,987.55]

print("list1:",l1)
print("list2",l2)

l1[-1]=l2

print("\nlist2:",l2)
print("list1:",l1)
#---------------------------------------
"""
SETS:
----------------------------
"""
#8)
set1={1,2,3,4,5,6,7,8,9,10}
print("set1:",set1)

value=int(input("Enter please a integer:"))
set1.add(value)
print("set1:",set1)
#----------------------------------------------------


#9)
set2={1,2,3,"ACA","python",True}
print("set2:",set2)

ri=input("Enter a value from the set2:")
set2.discard(ri)
print("set2:",set2)
#------------------------------------------------------


#10)
set2={1,2,3,"ACA","python",True}
print("set2:",set2)

ri=input("Enter a value from the set2:")
set2.remove(ri)
print("set2:",set2)
#---------------------------------------------------


#11)
set1={2,4,6,8,10,"python","c","c++","c#"}
set2={1,3,5,7,9,"python","java","javascrpt","php"}

print("The union sets:",set1.union(set2))
# #or-->(set1 | set2)
print("The intersaction sets:",set1.intersection(set2))
# #or-->(set1 & set2)
#-----------------------------------------------------------


#12)
set3={-5,-4,-3,-2,-1,0,1,2,3,4,5,}
print(set3)

minimum=min(set3)
maximum=max(set3)

v=int(input("Enter a integer:"))

print(v>=minimum and v<=maximum)
#------------------------------------------
"""
TUPLES:
---------------------------
"""
#13)
t1=1,2,3,4,5,6,7,8,9,10

print(t1[4])
print(t1[-4])
#--------------------------------------


#14)
t2=1,2,"py",True,34.32,3,4,5
print("tuple2:",t2)

t2=list(t2)
t2[4]="hello"
t2=tuple(t2)
print("tuple2:",t2)   
#--------------------------------------
"""
DICTIONARIES:
------------------------
"""
#15)
dict1={"key1":"value1","key2":"value2","key3":"value3"}
print("dict1 before updateing:",dict1)

key=input("Enter please a key:")
value=input("Enter please a value:")

dict1.update({key:value})
print("dict1 after updateing:",dict1)   
#-----------------------------------------------------------



#16)
l1=[(1,"a"),(2,"b"),(3,"c")]

d1={l1[0][0]:l1[0][1],l1[1][0]:l1[1][1],l1[2][0]:l1[2][1]}
print("d1:",d1)


