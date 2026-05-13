class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.price = price  # Uses the property setter for validation

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value