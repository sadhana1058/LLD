class BankAccount:
    def __init__(self,ownerName,accountNumber,balance):
        self.ownerName = ownerName
        self.accountNumber = accountNumber
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount>0:
            self._balance += amount
        return
    
    def withdraw(self,amount: float) -> None:
        if self._balance >= amount :
            self._balance -= amount
            return True
        return False
    def display_account(self):
        # Alice (SAV-001) | Balance: $1000.00
        print(f'{self.ownerName} {self.accountNumber} | Balance: ${self._balance:0.2f}')

class SavingsAccount(BankAccount):
    def __init__(self,ownerName,accountNumber,balance, interestRate):
        super().__init__(ownerName,accountNumber,balance)
        self.interestRate = interestRate

    def apply_interest(self) -> None :
        self._balance += self._balance*(self.interestRate/100)
        return
    
    def withdraw(self,amount: float) -> None:
        if self._balance >= 100+amount :
            self._balance -= amount
            return True
        return False
class CheckingAccount(BankAccount):
    def __init__(self,ownerName,accountNumber,balance,overdraftLimit):
        super().__init__(ownerName,accountNumber,balance)
        self.overdraftLimit = overdraftLimit

    
    def withdraw(self,amount: float) -> None:
        if self._balance+self.overdraftLimit >= amount :
            self._balance -= amount
            return True
        return False
 


if __name__ == "__main__":
    savings = SavingsAccount("Alice", "SAV-001", 1000, 2.0)
    savings.display_account()
    print(f"Withdraw $950: {str(savings.withdraw(950)).lower()}")
    savings.apply_interest()
    savings.display_account()

    print()

    checking = CheckingAccount("Bob", "CHK-002", 500, 300)
    checking.display_account()
    print(f"Withdraw $700: {str(checking.withdraw(700)).lower()}")
    checking.display_account()