


"""
CONDITIONALS:
--------------------
"""
#1)
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

print("The number ​%d is the greatest" %n1) if n1>n2 else print("The number %d is greatest" %n2)



#2)
a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))

if a<=0 or b<=0:
    print("Enter a valid sides!")
else:
    print("rectangle") if a!=b else print("square")



#3)
name=input("Enter a name:")
age=int(input("Enter a age:"))
password=input("Enter a password:")

if name=="Batman":
    print("Welcome Mr. Batman!")
else:
    if age<16:
        print("Dear %s, you are too young to register" %name)
    elif "*" not in password and "&" not in password:
        print("Please enter a different password")
        
        


#4)
d={"name": "Armen", "age": 15,"grades": [10, 8, 8, 4, 6, 7]}

is_there="weight" in d.keys()

if is_there:
    [print(d[i]) for i in d if i=="weight"]
else:
    n=input("Enter any number:")
    d.update({"weight":n})





"""
LOOPS:
-------------
"""
#5)
for i in range(101):
    if i%2==1:
        print("i=",i)
    


#6)
for i in range(7):
    if i==2 or i==6:
        continue
    print("i=",i)
        


#7)
for i in range(1,21):
    if i%3==0 and i%5==0:
        break
    print("i=",i)    



#8)
list1=[5, 7, -7, "abc", 2, 4, True, 3, 4, 6, 7, 7]

for i in list1:
    if i==3:
        break
    print(i)



#9)
correct_num=5
count=0
while True:
    count+=1
    guess=int(input("Enter a number:"))
    if guess==correct_num:
        print("That was a good guess!")
        break
    if count==10:
        break  



"""
LIST COMPREHENSION:
----------------------
"""
#10)
num=[7,8, 120, 25, 44, 20, 27]
print("list before removing evens:",num)

num=[x for x in num if x%2!=0]
print("list after removing evens:",num)       



#11)
list3=[x**2 for x in range(1,51)]
print("list3:",list3)


#12)
list1=[1,2,3,4,5,10,20,30,40,50,100,200,300,400,500]
print("list1:",list1)

list2=[x for x in list1 if x>20]
print("list2:",list2)



#13)
str1=input("Enter a string:")
print("str1:",str1)

l1=[letter for letter in str1]
print("l1:",l1)



#14)
list1=['a', 'abc', 'xyz', 's', 'aba','1221']

other_list=[item for item in list1 if len(item)>2 and item[0]==item[-1]]
print(len(other_list),"element: ",other_list)

