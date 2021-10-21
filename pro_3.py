#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


car = Bus("marcides", 120, 34)
print(
    f"car name is{car.name},it's max speed is {car.max_speed} and its millage is {car.mileage}"
)
