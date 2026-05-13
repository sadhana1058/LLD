from abc import ABC, abstractmethod


class Discount(ABC):
    def __init__(self, label: str):
        self._label = label

    @abstractmethod
    def apply(self, price: float) -> float:
        return price

    def describe(self, original_price: float):
        # TODO: call self.apply(original_price) and print:
        #   "label: $original_price -> $discounted_price"
        # Hint: use f"{value:.2f}" for formatting
        print(f'{self._label}: ${original_price:.2f} -> ${self.apply(original_price):.2f}')


class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        super().__init__(f"{percentage:.1f}% off")
        self._percentage = percentage
        # TODO: initialize self._percentage

    def apply(self, price: float) -> float:
        # TODO: return price * (1 - percentage / 100)
        return price*(1-(self._percentage)/100)


class FlatDiscount(Discount):
    def __init__(self, amount: float):
        super().__init__(f"${amount:.1f} off")
        # TODO: initialize self._amount
        self._amount = amount

    def apply(self, price: float) -> float:
        # TODO: return max(price - amount, 0)
        return max(price-self._amount,0)


class BuyOneGetOneFree(Discount):
    def __init__(self):
        super().__init__("Buy 1 Get 1 Free")

    def apply(self, price: float) -> float:
        # TODO: return price / 2
        return price/2


class OrderProcessor:
    def process_order(self, item_name: str, price: float, discount: Discount):
        # TODO: print "Item: item_name" then call discount.describe(price)
        print(f'Item: {item_name}')
        discount.describe(price)


if __name__ == "__main__":
    processor = OrderProcessor()

    processor.process_order("Laptop", 999.99, PercentageDiscount(20))
    processor.process_order("Headphones", 49.99, FlatDiscount(15))
    processor.process_order("Keyboard", 79.98, BuyOneGetOneFree())