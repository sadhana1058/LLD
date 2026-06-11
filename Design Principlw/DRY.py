from abc import ABC, abstractmethod

# 1. The Strategy Interface
class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        """Returns a tuple of (tax_amount, tax_rate)"""
        pass
        
    @abstractmethod
    def get_region(self) -> str:
        pass

# 2. Concrete Strategy Implementations
class USTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> tuple[float, float]:
        rate = 0.10
        return rate * amount
        
    def get_region(self) -> str:
        return 'US'

class EUTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> tuple[float, float]:
        rate = 0.20
        return rate * amount
        
    def get_region(self) -> str:
        return 'EU'

class UKTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> tuple[float, float]:
        rate = 0.15
        return rate * amount
        
    def get_region(self) -> str:
        return 'UK'

# 3. The Context Class (Accepting the Strategy via Dependency Injection)
class OrderProcessor:
    def __init__(self, tax_calculator: TaxCalculator):
        self.tax_calculator = tax_calculator
        self.region = tax_calculator.get_region()
    
    def process_order(self, amount: float) -> None:
        tax_amount = self.tax_calculator.calculate_tax(amount)
        total = amount + tax_amount
        
        # Displaying tax dollars and showing the rate in brackets for clarity
        print(f"{self.region} Order - Subtotal: ${amount:.2f}, Tax: ${tax_amount:.2f}, Total: ${total:.2f}")

# 4. Execution
if __name__ == "__main__":
    us_processor = OrderProcessor(USTaxCalculator())
    us_processor.process_order(100.0)
    
    eu_processor = OrderProcessor(EUTaxCalculator())
    eu_processor.process_order(100.0)
    
    uk_processor = OrderProcessor(UKTaxCalculator())
    uk_processor.process_order(100.0)