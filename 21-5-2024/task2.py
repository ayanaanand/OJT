class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_battery_info(self):
        return f"Battery Capacity: {self.battery_capacity} kWh"

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(my_electric_car.display_info())  
print(my_electric_car.display_battery_info())  
