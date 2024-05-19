# sports_car.py
from car import Car

class SportsCar(Car):
    def _init_(self, make, model, year, top_speed):
        super()._init_(make, model, year)
        self.top_speed = top_speed
        self.engine_running = False

    def get_info(self):
        return f"{self.year} {self.make} {self.model} with a top speed of {self.top_speed} mph"

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return "Engine started"
        return "Engine is already running"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Engine stopped"
        return "Engine is already off"

    def drive(self):
        if self.engine_running:
            return f"Driving the {self.make} {self.model} at {self.top_speed} mph"
        return "Start the engine first"

if _name_ == "_main_":
    sports_car = SportsCar("Ferrari", "488", 2021, 211)
    print(sports_car.get_info())
    print(sports_car.start_engine())
    print(sports_car.drive())
    print(sports_car.stop_engine())
