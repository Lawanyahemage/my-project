
from car import Car

class HybridCar(Car):
    def __init__(self, make, model, year, battery_size, fuel_type):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{self.year} {self.make} {self.model} with a {self.battery_size}-kWh battery and {self.fuel_type} fuel"

if __name__ == "__main__":
    h_car = HybridCar("Toyota", "Prius", 2022, 8.8, "gasoline")
    print(h_car.get_info())
