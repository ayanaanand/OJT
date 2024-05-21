class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        final_amount = total_fare + maintenance_charge
        return final_amount


vehicle = Vehicle(50)
print(f"Vehicle fare: {vehicle.fare()}")

bus = Bus(50)
print(f"Bus fare: {bus.fare()}")
