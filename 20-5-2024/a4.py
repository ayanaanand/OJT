class Vehicle:
    def __init__(self,model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Bus(Vehicle):
    vehicle_type = "Bus"  

    def __init__(self,model, year, capacity=50):
        super().__init__(model, year)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.capacity}")
        print(f"Vehicle Type: {Bus.vehicle_type}")

