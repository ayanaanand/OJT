class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Boat(Vehicle):
    def move(self):
        return "The boat sails on water."

class Car(Vehicle):
    def move(self):
        return "The car drives on the road."

class Plane(Vehicle):
    def move(self):
        return "The plane flies in the sky."

class Bike(Vehicle):
    def move(self):
        return "The bike is ridden on paths."

# Create instances of each class
vehicles = [Boat(), Car(), Plane(), Bike()]

# Demonstrate polymorphism
for vehicle in vehicles:
    print(vehicle.move())
