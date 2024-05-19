# main.py
from car import Car
from Hybrid_car import HybridCar
from electric_car import ElectricCar
from sports_car import SportsCar 

def main():
    # Create instances of each car type
    car = Car("Toyota", "Camry", 2020)
    hybrid = HybridCar("Toyota", "Prius", 2022, 8.8, "gasoline")
    electric = ElectricCar("Tesla", "Model S", 2022, 100)
    sports_car = SportsCar("Ferrari", "488", 2021, 211)

    # Print information about each car
    print(car.get_info())
    print(hybrid.get_info())
    print(electric.get_info())
    print(sports_car.get_info())

if __name__ == "__main__":
    main()



