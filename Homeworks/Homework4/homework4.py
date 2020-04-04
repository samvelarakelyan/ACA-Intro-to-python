


"""
CONDITIONALS:
--------------------
"""
#1)
n_shoes=int(input())

if n_shoes<=0:
    print("Invalid input!")
else:
    total_price=0
    total_price+=n_shoes*100
    print("You get adiscount") if total_price>1000 else print("You don't get a discount")



#2)
d={"name": "Armen", "age": 15, "grades": [10, 8, 8,4, 6, 7]}

sum_grades=sum(d["grades"])
len_grades=len(d["grades"])

print("Good job!") if sum_grades/len_grades>7 else print("You need to work more") 


"""
LOOPS AND LOOP CONTROL STATEMENTS:
---------------------------------
"""
#3)
for i in range(11):
    if i%2==0:
        continue
    print(i)


#4)
list1 = [1, 3, 5, 7, 9, 11, 13, 15]
list2 = [4, 6, 14, 11, 8, 16]

for item in list1:
    if item in list2:
        break
    print("item:",item)



#5)
menu=['ice cream', 'chocolate', 'apple crisp', 'cookies']
while True:
    desert=input("Enter a desert:")
    if desert in menu:
        print("Your desert will arrive in 10 minutes")
        break
    print("Please choose another desert")



"""
LIST COMPREHENSION:
--------------------
"""
#6)
list2=[1,2,3,4,5,6,7,8,9,10]

other_list=[item for item in list2 if item>=5 and item<=10]
print(len(other_list),"element: ",other_list)



#7)
list4= [[10, 20, 40], [40, 50, 60],[70, 80, 90]]
print("list4:",list4)

list5=[[100 if i==item[-1] else i for i in item] for item in list4]
print("list5:",list5)





















