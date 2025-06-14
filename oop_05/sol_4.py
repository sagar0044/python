# ENCAPSULATION.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla=ElectricCar("TeslA","ModelS","85KW")
my_car=Car("pulsar","ns")
print(my_car.fuel_type())
print(my_tesla.brand)
print(my_tesla.fuel_type())