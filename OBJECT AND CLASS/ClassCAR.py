
# 1. Define the Class (The Blueprint)
class Car:
    # Class attribute (shared by all instances)
    category = "Automobile"

    # Constructor method to initialize instance attributes
    def __init__(self, brand, model, year):
        self.brand = brand    # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute

    # Instance method (action the object can perform)
    def display_info(self):
        return f"{self.year} {self.brand} {self.model} ({self.category})"

    # Another instance method
    def start_engine(self):
        return f"The engine of the {self.model} is now running."


# 2. Create Objects (Instances of the Class)
car1 = Car("Toyota", "Corolla", 2024)
car2 = Car("Tesla", "Model 3", 2025)


# 3. Access Attributes and Call Methods
print(car1.display_info())   # Output: 2024 Toyota Corolla (Automobile)
print(car2.start_engine())   # Output: The engine of the Model 3 is now running.

# Accessing attributes directly
print(f"Car 1 Brand: {car1.brand}")  # Output: Car 1 Brand: Toyota
print(f"Car 2 Brand: {car2.brand}")  # Output: Car 2 Brand: Tesla