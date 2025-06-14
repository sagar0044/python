class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
my_car=Car("pulsar","ns")
print(my_car.full_name())
print(my_car.brand)