class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f"Vehicle: {self.brand} {self.model} ({self.year})")


class ElectricCar(Vehicle):
    def __init__(self,brand,model,year,battery_capacity):
        super().__init__(brand,model,year)
        self.battery_capacity=battery_capacity

    def display(self):
        super().display()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

class GasCar(Vehicle):
    def __init__(self,brand,model,year,fuel_capacity):
        super().__init__(brand,model,year)
        self.fuel_capacity=fuel_capacity

    def display(self):
        super().display()
        print(f"Fuel Capacity: {self.fuel_capacity} liters")


if __name__ == "__main__":
    electric_car = ElectricCar("Tesla", "Model S", 2020, 100)
    gas_car = GasCar("Toyota", "Camry", 2019, 50)

    electric_car.display()
    print()
    gas_car.display()