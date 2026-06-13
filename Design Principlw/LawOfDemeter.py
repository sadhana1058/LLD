class Address:
    def __init__(self, city):
        self._city = city

    def get_city(self):
        return self._city

class Customer:
    def __init__(self, address):
        self._address = address

    def get_address(self):
        return self._address

    def get_city(self):
        if self._address is None:
            return "Unknown"
        return self._address.get_city()

class CreditCard:
    def __init__(self, last_4_digits):
        self._last_4_digits = last_4_digits

    def get_last_4_digits(self):
        return self._last_4_digits

class Payment:
    def __init__(self, credit_card):
        self._credit_card = credit_card

    def get_credit_card(self):
        return self._credit_card

    def get_last_4_digits(self):
        if self._credit_card is None:
            return "Unknown"
        return self._credit_card.get_last_4_digits()

class Order:
    def __init__(self, customer, payment):
        self._customer = customer
        self._payment = payment

    def get_customer_city(self):
        if self._customer is None:
            return "Unknown"
        return self._customer.get_city()

    def get_payment_last_4_digits(self):
        if self._payment is None:
            return "Unknown"
        return self._payment.get_last_4_digits()

    def get_customer(self):
        return self._customer

    def get_payment(self):
        return self._payment

class OrderSummaryPrinter:
    def print_summary(self, order):
        city = order.get_customer_city()
        last4 = order.get_payment_last_4_digits()

        print(f"Ship to: {city}")
        print(f"Paid with card ending in: {last4}")

if __name__ == "__main__":
    address = Address("San Francisco")
    customer = Customer(address)
    card = CreditCard("4242")
    payment = Payment(card)
    order = Order(customer, payment)

    printer = OrderSummaryPrinter()
    printer.print_summary(order)