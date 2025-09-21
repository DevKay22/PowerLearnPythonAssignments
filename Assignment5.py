# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with their own implementations of move()
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water!")

class Bike(Vehicle):
    def move(self):
        print("🚴 Riding through the streets!")

# Demonstration of polymorphism
def show_vehicle_movement(vehicles):
    for v in vehicles:
        v.move()  # Polymorphic behavior

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat(), Bike()]

# Call the function
show_vehicle_movement(vehicles)
