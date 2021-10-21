#Define property that should have the same value for every class instance
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus1 = Bus("School Volvo", 180, 12)
print(
    f"Color:{bus1.color}, Vehicle name:{bus1.name} ,Speed:{bus1.max_speed}, Mileage:{bus1.mileage}"
)
car1 = Car("Audi Q5", 240, 18)
#Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
#Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18