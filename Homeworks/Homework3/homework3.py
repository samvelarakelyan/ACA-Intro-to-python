


"""
LISTS:
----------------------
"""
#1)
a=[1,4,5,7,8,-2,0,-1]
print("a=",a)
#---------------------------------------


#2)
print("a[3]=",a[3],"\ta[5]=",a[5])
#---------------------------------------


#3)
a_sorted=a.copy()
a_sorted.sort(reverse=True)

print("a_sorted=",a_sorted)
#---------------------------------------


#4)
print("sublist_1_3=",a_sorted[0:3])
print("sublist_2_6=",a_sorted[1:6])    
#--------------------------------------


#5)
a_sorted.pop(2)
a_sorted.pop(3)
#------------------------------------


#6)
print("a_sorted=",a_sorted) 
#----------------------------------------------


#7)
b=["grapes", "Potatoes","tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
print("b=",b)
#---------------------------------------------------------------


#8)
b_sorted=b.copy()
b_sorted.sort()
print("b_sorted=",b_sorted)
#----------------------------------------------------------------


#9)
c=a[0:3]+b[3:6]
#------------------------

#10)
print("c=",c)
#------------------------


"""
SETS:
--------------------------
"""
#1)
a1=["Cookies", "Chocolate",8, True, -3, -5, "Chocolate", 8, False, 8]
print("a1=",a1)
#-------------------------------------------------------

#2)
b1=[8, True, 10, 14,"Chocolate", "Milk", "Jelly", True, False, True]
print("b1=",b1)
#-------------------------------------------------------

#3)
set_a=set(a1)
print("set_a",set_a)
#-----------------------------------------

#4)
set_b=set(b1)
print("set_b=",b1)
#-----------------------------------------

#5)
union_ab=set_a.union(set_b)
#or-->(set_a | set_b)
print("union_ab=",union_ab)
#-----------------------------------------------

#6)
intersection_ab=set_a.intersection(set_b)
#or-->(set_a & set_b)
print("intersection_ab=",intersection_ab)
#-----------------------------------------------

#7)
union_ab.add("Kit-Kat")
union_ab.add("Oreo")
print("union_ab after update:",union_ab)
#-----------------------------------------------

#8)
new_set=union_ab or intersection_ab
print("new set:",new_set)
#----------------------------------------------

#9)
print("Chocolate" in new_set)
#--------------------------------------------

#10)
new_set.remove("Oreo")
print("new_set:",new_set)
#---------------------------------------------


"""
TUPLES:
----------------------
"""
#1)
t1=1,True,"a",-2,"Anna"
print("t1:",t1)


#2)
t1=list(t1)
# t1.remove(True) --> in this case it's wrong,deletes int 1
t1.pop(1)
t1=tuple(t1)
print("t1:",t1)


#3)
t2=1,2,3,4,5
print("t2:",t2)


#4)
t3=t1[0],t1[1],1,2,3
print("t3:",t3)


#5)
print("t3[2]=",t3[2])


#6)
t4=[(1,3,5), (8,9), ("Anna", "Bob","Alice")]
print("t4:",t4)
print(t4[0][1])


"""
DICTIONARIES:
-----------------------
"""
market={"dairy":["yogurt", "cheese"], "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana","banana"]}
print("market before updateing:",market)

market.update({"candies":["mars","kinder","twix"]})
print("market after updateing:",market)

market["fruits"]=list(set(market["fruits"]))
market["fruits"].sort()
print(market)

