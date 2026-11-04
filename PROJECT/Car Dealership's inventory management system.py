# SCENARIO: Car dealershhip's inventory management system


#Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.
#Task-2. Update the class with the default color for all vehicles," white"
#Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle. 
#Task-4. Create a method to display all the properties of an object of the class.
#Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, and another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.¶

class Vehicle:
    color = "white"
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
        self.seating_capacity = None


    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print(f"Color: {self.color}")
        print(f"Max speed: {self.max_speed}")
        print(f"Milage: {self.milage}")
        print(f"Seating capacity: {self.seating_capacity}")

# Creating objects of the Vehicle class
Vehicle1 = Vehicle(200, 20)
Vehicle1.assign_seating_capacity(5)
Vehicle1.display_properties()

Vehicle2 = Vehicle(180, 25)
Vehicle2.assign_seating_capacity(4)
Vehicle2.display_properties()
