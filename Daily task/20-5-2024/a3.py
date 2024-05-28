class Vehicle:
    def __init__(self,model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Bus(Vehicle):
    def __init__(self, make, model, year, capacity=50):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.capacity}")
