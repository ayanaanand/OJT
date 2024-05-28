class Adit:
    def __init__(self):
        self.name = None
        self.phone_number = None
    
    def store_info(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")


