# Basic class and object.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model= model
my_car=Car("toyota","corolla")
print(my_car.brand)
print(my_car.model)