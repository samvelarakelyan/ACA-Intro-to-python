


#1)
class Circle:
    def __init__(self, radius:float, color:str):
        self.radius = radius
        self.color = color
        
    def getDesc(self):
        print("A %s color circle with radius %.2f" %(self.color, self.radius))
        
        

c1 = Circle(3.14, "red")
c2 = Circle(6.28, "green")
c3 = Circle(9.42, "blue")
c4 = Circle(3.141592, "black")
c5 = Circle(18, "White")

c1.getDesc()
c2.getDesc()
c3.getDesc()
c4.getDesc()
c5.getDesc()




#2)
class String:
    def __init__(self, my_str:str):
        self.my_str = my_str
    
    def get_String(self):
        return self.my_str
    
    def print_String(self):
        print(self.my_str.upper())
    
    
s1 = String("pyhton")
s2 = String("c/c++, java, c#")
s3 = String("1_SpaceX_1")
s4 = String("_-_-_-12345_-_-_-")
s5 = String("!@#$%^&*()")

#for s1 object 
print("\nget_String: ",s1.get_String())
print("print_String: ", end = '')
s1.print_String()

#for s2 object 
print("\nget_String: ",s2.get_String())
print("print_String: ", end = '')
s2.print_String()

#for s3 object 
print("\nget_String: ",s3.get_String())
print("print_String: ", end = '')
s3.print_String()

#for s4 object 
print("\nget_String: ",s4.get_String())
print("print_String: ", end = '')
s4.print_String()

#for s5 object 
print("\nget_String: ",s5.get_String())
print("print_String: ", end = '')
s5.print_String()





#3)
class Employee:
    def __init__(self, name:str, lastname:str, monthly_salary:int):
        self.name = name
        self.lastname = lastname
        self.__monthly_salary = monthly_salary
        
    def get_FullName(self):
        return self.name, self.lastname
    
    
    def annualSalary(self):
        annual_salary = 12 * self.__monthly_salary
        return "Higt" if annual_salary > 100 else "Low"
    


e1 = Employee("Poxos", "Poxosyan", 6)
e2 = Employee("Petros", "Petrosyan", 9)

print("\nFull name: %s\nAnnual salary: %s\n" %(e1.get_FullName(), e1.annualSalary()))
print("Full name: %s\nAnnual salary: %s\n" %(e2.get_FullName(), e2.annualSalary()))





#4)
class Car:
    def __init__(self, model:str, color:str, max_speed:int):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        
    def compareCar(self, car2):
        if self.max_speed > car2.max_speed:
            return "car1 is better then car2"
        return "cra2 is better then car1"
    

tesla = Car("Tesla Roadster", "black", 400)
bmw = Car("BMW x7", "black", 260)
mercedes = Car("Mercedes c class", "grey", 240)

print(tesla.compareCar(bmw))
print(bmw.compareCar(mercedes))
print(mercedes.compareCar(tesla))

        


#5)
class Police_car:
    tax_value = 0.2
    
    def __init__(self, owner:str, price:int, pass_code:str):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code
        
    def set_pass_code(self, pass_code):
        self.__pass_code = pass_code
        
    def get_pass_code(self):
        return self.__pass_code
        
    def tax(self):
        return self.tax_value * self.price
    
    def greating(self):
        if self.__pass_code == "admin":
            print("Welcom to your car,",self.owner)
        
        

car1 = Police_car("kaptin Poghosyan", 3000, "code")

print("\ncar1:\npass code before changing: ", car1.get_pass_code()) #print pass code before changing
print("pass code after changing: ", end = '') 
car1.set_pass_code("other code") #changing pass code using class's set function
print(car1.get_pass_code()) #print pass code after changing 
print(car1.tax())
car1.greating() #doesn't print anything


car2 = Police_car("major Petrosyan", 4500, "code2")

print("\ncar2:\npass code before changing: ", car2.get_pass_code()) #print pass code before changing
print(car2.tax())
car2.greating() #doesn't print anything
car2.set_pass_code("admin") #changing pass code using class's set function
print(car2.get_pass_code()) #print pass code after changing 
car2.greating() #print "Welcom to your car, major Petrosyan"
print("")


"""
INHERITANCE
------------
"""
#6)
class Animal:
    def __init__(self, name:str):
        self.name = name
        
    def move(self):
        print("I can move") 


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "Dog")
    def move(self):
        print("I can run really fast")
                

dog = Dog()
dog.move()
        
    


#7)
class Animal:
    def __init__(self, name:str, legs:int):
        self.name = name
        self.legs = legs
        
    def getName(self):
        print("\nMy name is %s" %self.name)
        
    def getLegs(self):
        print("I have %d legs" %self.legs)
        
        
        
class Exnik(Animal):
    def __init__(self):
        Animal.__init__(self, "Exnik", 4)
        

exnik = Exnik()
exnik.getName()
exnik.getLegs()


#8)
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name:str, weight:float):
        self.name = name
        self.weight = weight
        
    @abstractmethod
    
    def fly(self):
        pass
    

class Hav(Bird):
    def __init__(self, name:str, weight:float):
        super().__init__(name, weight)
        
    def fly(self):
        print("I believe i can fly")
        
    

havik = Hav("Chalo", 6.5)
havik.fly()    
    
