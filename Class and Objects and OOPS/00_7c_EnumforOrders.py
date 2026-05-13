from enum import Enum

class OrderStatus(Enum):
    PLACED = "PLACED"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class PaymentMethod(Enum):
    CREDIT_CARD = ("Credit Card", 2.5)
    DEBIT_CARD = ("Debit Card", 1.0)
    UPI = ("UPI", 0.0)
    NET_BANKING = ("Net Banking", 1.5)

    def __init__(self, display_name: str, fee_percent: float):
        self.display_name = display_name
        self.fee_percent = fee_percent

class Order:
    _status_transitions = {
        OrderStatus.PLACED: OrderStatus.CONFIRMED,
        OrderStatus.CONFIRMED: OrderStatus.SHIPPED,
        OrderStatus.SHIPPED: OrderStatus.DELIVERED,
    }

    def __init__(self, order_id: str, payment_method: PaymentMethod, amount: float):
        self._order_id = order_id
        self._status = OrderStatus.PLACED
        self._payment_method = payment_method
        self._amount = amount

    def advance_status(self) -> bool:
        next_status = self._status_transitions.get(self._status)
        if next_status:
            self._status = next_status
            return True
        return False

    def cancel(self) -> bool:
        if self._status in (OrderStatus.PLACED, OrderStatus.CONFIRMED):
            self._status = OrderStatus.CANCELLED
            return True
        return False

    def get_total_with_fees(self) -> float:
        return self._amount + (self._amount * self._payment_method.fee_percent / 100)

    def display_info(self) -> None:
        print(f"Order {self._order_id} | Status: {self._status.value} | "
              f"Payment: {self._payment_method.display_name} | "
              f"Amount: ${self._amount:.2f} (with fees: ${self.get_total_with_fees():.2f})")


if __name__ == "__main__":
    order = Order("ORD-001", PaymentMethod.CREDIT_CARD, 99.99)
    order.display_info()

    order.advance_status()  # PLACED -> CONFIRMED
    order.advance_status()  # CONFIRMED -> SHIPPED
    order.display_info()

    print(f"Cancel after shipping: {order.cancel()}")  # False