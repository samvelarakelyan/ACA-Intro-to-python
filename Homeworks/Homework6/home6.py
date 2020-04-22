


class Person:
    def __init__(self, name:str, last_name:str, age:int, gender:str, student:bool, password:str):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password
        
    def set_password(self, new_password):
        self.__password = new_password
        
    def get_password(self):
        return self.__password
        
    def Greeting(self, second_person):
        print("Welcome dear", self.name)
    
    def Goodbye(self):
        print("Bye everyone!")
        
    def Favourite_num(self, num1:int):
        return "My favoutite number is " + str(num1)
    
    def Read_file(self, filename:str):
        filename+=".txt"
        file = open(filename, mode = 'r', encoding = 'utf-8')
        for letter in file:
            print(letter, end = '')
        
                
person = Person("Poghos", "Poghosyan", 120, "mael", True, "password")




#2)
class Calculation:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        
    def addition(self):
        print("%d + %d = %d" %(self.x, self.y, self.x + self.y))
        
    def subtraction(self):
        print("%d - %d = %d" %(self.x, self.y, self.x - self.y))
        
    

class MyCalculation(Calculation):
    def __init__(self, x:int, y:int):
        Calculation.__init__(self, x, y)
    
    def multiplication(self):
        print("%d * %d = %d" %(self.x, self.y, self.x * self.y))
        
    def division(self):
        print("%d / %d = %.2f" %(self.x, self.y, self.x / self.y))



c = MyCalculation(3, 5)

c.addition()
c.subtraction()
c.multiplication()
c.division()
        


#3)
class My_Time:
    def __init__(self, t:str):
        self.t = t
        
    def printTime(self):
        print("The current time is ",self.t)
        
    
    
class My_Date:
    def __init__(self, d:str):
        self.d = d
        
    def printDate(self):
        print("The current date is ",self.d)
        
    
    
class Date_Time(My_Time, My_Date):
    def __init__(self, t:str, d:str):
        My_Time.__init__(self, t)
        My_Date.__init__(self, d)
        

dt = Date_Time("12 PM", "13.03.2013")

dt.printTime()
dt.printDate()

    
    
#4)
class Model:
    def __init__(self, name):
        self.name = name

    def printModel(self):
        print("The model of the vehicle is", self.name)
    

class Color:
    def __init__(self, color):
        self.color = color
        
    def printColor(self):
        print("The color of the vehicle is", self.color)
    

class Car(Model, Color):
    def __init__(self, model, color):
        Model.__init__(self, model)
        Color.__init__(self, color)
        

car_bmw = Car("BMW", "red")

car_bmw.printModel()
car_bmw.printColor()


        













