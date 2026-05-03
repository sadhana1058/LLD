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

class BankAccount:
    def __init__(self, account_holder: str):
        self.__account_holder = account_holder
        self.__balance = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def account_holder(self) -> str:
        return self.__account_holder