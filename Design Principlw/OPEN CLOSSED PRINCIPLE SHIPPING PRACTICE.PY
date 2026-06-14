from abc import ABC,abstractmethod
class ShippingStrategy(ABC):
    @abstractmethod
    def calculateCost(self,weight):
        pass
class StandardShipping(ShippingStrategy):
    def calculateCost(self,weight):
        return weight * 1.5


class ExpressShipping(ShippingStrategy):
    def calculateCost(self,weight):
        return weight * 3

class OvernightShipping(ShippingStrategy):
    def calculateCost(self,weight):
        return weight * 5

class InternationalShipping(ShippingStrategy):
    def calculateCost(self,weight):
        return weight * 10

class ShippingCostCalculator:
    def calculate(self, shipping_type:ShippingStrategy, weight: float) -> float:
        return shipping_type.calculateCost(weight)
            
        # raise ValueError(f"Unknown shipping type: {shipping_type}")

# Usage
calculator = ShippingCostCalculator()
print(f"Standard: ${calculator.calculate( StandardShipping(), 2.0)}")
print(f"Express: ${calculator.calculate(ExpressShipping(), 2.0)}")
print(f"Overnight: ${calculator.calculate(OvernightShipping(), 2.0)}")
print(f"International: ${calculator.calculate(InternationalShipping(), 2.0)}")

# TODO: Define a ShippingStrategy interface (ABC) with a calculate_cost(weight) method.
# TODO: Create concrete implementations for each shipping type.
# TODO: Refactor ShippingCostCalculator to accept a ShippingStrategy.