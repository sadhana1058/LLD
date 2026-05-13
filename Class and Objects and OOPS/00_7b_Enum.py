from enum import Enum

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    
    def __init__(self, value):
        self.c = value
    
    def get_value(self):
        return self.c
total = Coin.DIME.get_value() + Coin.QUARTER.get_value()  # 35
print(total)