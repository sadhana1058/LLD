from enum import Enum

class OrderStatus(Enum):
    PLACED=0
    CONFIRMED = 2
    SHIPPED =1
    DELIVERED=4

OrderStatus.SHIPPED =5

print(OrderStatus.SHIPPED.value)
