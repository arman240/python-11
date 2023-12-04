class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed doesn't go below 0
        self.current_speed = max(0, self.current_speed + speed_change)
        # Ensure speed doesn't exceed the maximum
        self.current_speed = min(self.current_speed, self.max_speed)

    def drive(self, hours):
        # Calculate the distance traveled based on constant speed
        distance_traveled = self.current_speed * hours
        # Update the travelled distance
        self.travelled_distance += distance_traveled

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

# Main program
if __name__ == "__main__":
    # Create an ElectricCar and a GasolineCar
    electric_car = ElectricCar(registration_number="ABC-15", max_speed=180, battery_capacity=52.5)
    gasoline_car = GasolineCar(registration_number="ACD-123", max_speed=165, tank_volume=32.3)

    # Select speeds for both cars
    electric_car.accelerate(40)  # Set electric car speed to 40 km/h
    gasoline_car.accelerate(50)  # Set gasoline car speed to 50 km/h

    # Make both cars drive for three hours
    electric_car.drive(3)
    gasoline_car.drive(3)

    # Print out the values of their kilometer counters
    print(f"Electric Car Kilometer Counter: {electric_car.travelled_distance} km")
    print(f"Gasoline Car Kilometer Counter: {gasoline_car.travelled_distance} km")
