


"""
Assertions
----------
"""
#1)
def Alarm(day:str):
    assert day != "Sunday", "I won't wake you up today!"



#2)
def sum(x:int, y:int):
    assert isinstance(x,int) and isinstance(y,int), "Arguments of type int required"
    return x + y


"""
Exceptions:
----------
"""
#1)
def div1(x:int, y:int):
    try:
        return x / y
    except Exception:
        return "Error: divisor can't be zero"



#2)
def div2(x:int, y:int):
    try:
        return x / y
    except ZeroDivisionError as zde:
        return zde



#3)
l = ["a", 0, 2]

try:
    for item in l:
        print("The current entry is: {0}".format(item))
        print("The resiprocal of {0} is {1}".format(item,1/item))
except ZeroDivisionError as zde:
    print("Oops! ",zde)
except TypeError as te:
    print("Oops! ",te)
    


#4)
username = input("Enter your name: ")

try:
    if username != "Rembo":
        print("Welcom,", username)
    else:
        raise Exception
except Exception:
    print("Rembo is an invalid username")




#5)
def get_value(data_list:list, index:int):
    try:
        print("returning the value")
        result = data_list[index]
        return result
    except IndexError as ie:
        return ie

    

#6)
def YourAge():
    try:
        age = int(input("Enter please your age: "))
        if age >= 0:
            print("I see that you are %d years old" %age)
        else:
            raise Exception
    except Exception:
        print("Error: age couldn't be negative!")

        
        





    









