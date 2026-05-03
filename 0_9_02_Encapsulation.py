class PaymentProcessor:
    def __init__(self, card_number: str, amount: float):
        self.__card_number = self.__mask_card_number(card_number)
        self.__amount = amount

    def __mask_card_number(self, card_number: str) -> str:
        return "****-****-****-" + card_number[-4:]

    def process_payment(self) -> None:
        print(f"Processing payment of ${self.__amount} for card {self.__card_number}")


if __name__ == "__main__":
    payment = PaymentProcessor("1234567812345678", 250.00)
    payment.process_payment()