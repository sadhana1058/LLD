from abc import ABC, abstractmethod

# ShippingStrategy interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass

# Concrete strategies
class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 1.5

class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 3.0

class OvernightShipping(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 5.0

class InternationalShipping(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 10.0

# Refactored calculator - no if-else
class ShippingCostCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate(self, weight: float) -> float:
        return self.strategy.calculate_cost(weight)

# Main
if __name__ == "__main__":
    weight = 2.0

    standard = ShippingCostCalculator(StandardShipping())
    express = ShippingCostCalculator(ExpressShipping())
    overnight = ShippingCostCalculator(OvernightShipping())
    international = ShippingCostCalculator(InternationalShipping())

    print(f"Standard: ${standard.calculate(weight)}")
    print(f"Express: ${express.calculate(weight)}")
    print(f"Overnight: ${overnight.calculate(weight)}")
    print(f"International: ${international.calculate(weight)}")