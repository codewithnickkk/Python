#Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel): #__init__ constructor
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f'{self.__brand} {self.__model}'
    
    def fuel_type(self):
        return 'petrol or deisel'
    
    @staticmethod
    def general_description():
        return 'cars are means of transport'
    
    @property
    def model(self):
        return self.__model
        
my_car = Car('toyota', 'corolla')
#print(my_car.brand, my_car.model)


#Problem 02: Add a method to the Car class that displays the full name of the car (brand and model).

name = Car('Tata','Safari')
print(name.full_name()) 

#Problem 03: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return 'electricity'

tesla_car = ElectricCar('tesla', 'model s', '85kw')
print(tesla_car.full_name())

#Problem 04: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

#__name --> ( __ ) this makes an attribute private
#getter is used to call private method or Attribute
# encapsulation --> avail for its class but not accessible to everyone 

print(tesla_car.get_brand())

#get_br.. getter method
#setter method (self learn)

#Problem 05: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
#polymophism --> aneik roop ---> example '+' adds integer and also concatinates srtings
 
mercedes_benz = ElectricCar('mercedes','benz','90kw')
toyota = Car('toyota','belta')

print(mercedes_benz.fuel_type())
print(toyota.fuel_type())

#Problem 06: Add a class variable to Car that keeps track of the number of cars created.
#adding variable total_car in Car()

print(Car.total_car) #also counts inheritance

#Problem 07: Add a static method to the Car class that returns a general description of a car. 

#static method is a method which belongs to the class rather than its instances/object of the class
print(toyota.general_description())
# print(Car.general_description())


#Problem 08: Use a property decorator in the Car class to make the model attribute read-only.
#make model private
# toyota.model = 'nexon' #cannot overwrite
print(toyota.model)

#Problem 09: Demonstrate the use of isinstance() to check if mercedes_benz is an instance of Car and ElectricCar.
#isinstance method throws boolean values
print(isinstance(mercedes_benz, Car))
print(isinstance(mercedes_benz, ElectricCar))

#Problem 10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def Engine_info(self):
        return "this is engine"
    
class ElectricCar2(Battery, Engine, Car):
    pass

my_tesla = ElectricCar2('tesla', 'model_s')
print(my_tesla.battery_info())
print(my_tesla.Engine_info())
    