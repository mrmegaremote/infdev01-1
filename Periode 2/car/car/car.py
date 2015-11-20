class car:
    def __init__ (self, engine, seat, light, people, wheels): 
        car.engine = engine
        car.seat = seat
        car.light = light
        car.people = people
        car.wheels = wheels

class engine:
    def __init__(self, power, rpm, fuel):
        engine.power = power
        engine.rpm = rpm
        engine.fuel = fuel

class seat:
    def __init__(self, fabric, shape):
        seat.fabric = fabric
        seat.shape = shape

class light:
    def __init__(self, color1, color2):
        light.frontlight = color1
        light.backlight = color2

class people:
    def __init__ (self, person1, person2):
        people.driver = person1
        people.passenger = person2

class wheels:
    def __init__ (self, wheel):
        wheels.tire = tire(3)
        wheels.Wheel1 = wheel
        wheels.Wheel2 = wheel
        wheels.Wheel3 = wheel
        wheels.Wheel4 = wheel

class tire:
    def __init__(self, pressure):
        tire.pressure = pressure

vehicle = car(engine(200, 5000, 30), seat("suave", "chair"), light("white", "red"), people("Driver", "Passenger"), wheels("wheel"))

print vehicle.wheels.tire.pressure
