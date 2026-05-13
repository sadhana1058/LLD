class ShoppingCart:
    def __init__(self):
        self._items: dict[str, float] = {}
        self._discount_applied = False
        self._is_checked_out = False

    def add_item(self, name: str, price: float) -> None:
        # Add item to cart, but reject if already checked out
        if self._is_checked_out:
            print("Cannot modify a checked-out cart.")
            return
        self._items[name] = self._items.get(name,0)+price
    def apply_discount(self, code: str) -> bool:
        # If code is "SAVE10" and no discount applied yet and not checked out,
        # mark discount as applied and return True. Otherwise return False.
        if not self._discount_applied:
            self._discount_applied=True
            return True
        return False

    def get_total(self) -> float:
        # Sum all item prices. If discount was applied, subtract 10%.
        total = sum(self._items.values())
        if self._discount_applied:
            total = 0.9*total
        return total

    def checkout(self) -> None:
        # Mark cart as checked out (only if it has items and isn't already checked out)
        if self._items and not self._is_checked_out:
            self._is_checked_out=True


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)
    # cart._items["Keyboard"] = 79.99  
    # Should be avoided (direct access to internal dict)

    print(f"Total: ${cart.get_total():.2f}")                     # 1029.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # true
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # false

    cart.checkout()
    cart.add_item("Keyboard", 79.99)  # Should be rejected
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98