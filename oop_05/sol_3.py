# INHERITANCE.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_tesla=ElectricCar("TeslA","ModelS","85KW")
my_car=Car("pulsar","ns")
print(my_car.full_name())
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name())