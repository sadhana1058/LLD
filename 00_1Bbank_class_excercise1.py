class BankAccount:
    def __init__(self,accountNumber,ownerName):
        self._accountNumber = accountNumber
        self._ownerName = ownerName
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
    
    def getBalance(self):
        return self.__balance

acc=BankAccount("123456789", "John Doe", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Current balance: {acc.getBalance()}")
