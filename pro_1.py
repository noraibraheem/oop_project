#Create a Vehicle class with max_speed and mileage instance attributes


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


car1 = Vehicle(200, 34)
print(car1.max_speed, car1.mileage)
