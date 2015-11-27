import Race
class Car:
    def __init__ (self, engine, seat, light, people, wheels): 
        self.engine = engine
        self.seat = seat
        self.light = light
        self.people = people
        self.wheels = wheels

class Engine:
    def __init__(self, power, rpm, fuel):
        self.power = power
        self.rpm = rpm
        self.fuel = fuel

class Seat:
    def __init__(self, fabric, shape):
        self.fabric = fabric
        self.shape = shape

class Light:
    def __init__(self, color1, color2):
        self.frontlight = color1
        self.backlight = color2

class People:
    def __init__ (self, person1, person2):
        self.driver = person1
        self.passenger = person2

class Wheels:
    def __init__ (self, wheel, brand):
        self.tire = Tire(3)
        self.frontright = wheel
        self.frontleft = wheel
        self.backright = wheel
        self.backleft = wheel
        self.brand = brand
class Wheel1:
    def __init__ (self, wheel, brand):
        self.tire = Tire(3)
        self.frontright = wheel
        self.brand = brand

class Tire:
    def __init__(self, pressure):
        self.pressure = pressure

vehicle = Car(Engine(200, 5000, 30), Seat("suave", "chair"), Light("white", "red"), People("Karel", "Hans"), Wheels("wheel", "Michelin"))

print 

