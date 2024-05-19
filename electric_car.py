# electric_car.py
from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_info(self):
        return f"{self.year} {self.make} {self.model} with a {self.battery_size}-kWh battery"

if __name__ == "__main__":
    e_car = ElectricCar("Tesla", "Model S", 2022, 100)
    print(e_car.get_info())
