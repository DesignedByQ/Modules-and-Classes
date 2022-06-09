'''# 1)Create a Vehicle class with max_speed and mileage instance attributes

# 2) Create a Vehicle class without any variables and methods

# 3) Create a child class Bus that will inherit all of the variables and methods of the 1st Vehicle class
# 4) Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.

# 5) Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

# 6) Define property that should have the same value for every class instance
# (Define a class attribute”colour” with a default value white)

#7) Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#Note: The bus seating capacity is 50. so the final fare amount should be 5500.
# You need to override the fare() method of a Vehicle class in Bus class.'''

class Vehicles:  
    def __init__(self, max_speed=30, mileage=000000, colour = "yellow", transmission = "automatic"):
        self.max_speed = max_speed
        self.mileage = mileage 
        self.colour = colour
        self.transmission = transmission

class Bus(Vehicles):
    def __init__(self, max_speed, mileage, colour, transmission, manufacturer):
        super().__init__(max_speed, mileage, colour, transmission)
        self.manufacturer = manufacturer

vehicle1 = Bus(100, 50219, "black", "manual", "audi")

print(vehicle1.__dict__)
        