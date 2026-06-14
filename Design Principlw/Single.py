# Before: One class doing three unrelated jobs

class InventoryManager:
    def __init__(self):
        self.inventory = {"LAPTOP": 10, "PHONE": 25, "TABLET": 15}
    def check_inventory(self,product_id,quantity):
        stock = self.inventory.get(product_id, 0)
        if stock < quantity:
            print(f"Insufficient stock for {product_id}")
            return -1
        return stock
class NotificationService:
    def notify(self,customer_email,order_id,total):
        print(f"Email to {customer_email}: Order {order_id} confirmed. Total: ${total}")

class OrderService:
    def __init__(self):
        self.orders = []
    def process_order(self,quantity: int):
        price_per_unit = 100.0
        total = price_per_unit * quantity
        order_id = f"ORD-{len(self.orders) + 1}"
        self.orders.append(order_id)
        return total,order_id
        
    
    # def place_order(self, product_id: str, quantity: int, customer_email: str):
class OrderProcessor:
    def __init__(self,inv:InventoryManager,notification:NotificationService):
        self.inv = inv
        self.notification = notification

    def place_order(self, product_id: str, quantity: int, customer_email: str):
        # Responsibility 1: Inventory check
        
        order = OrderService()
        stock = self.inv.check_inventory(product_id,quantity)
        # Responsibility 2: Order processing
        if stock==-1:
            return
        self.inv.inventory[product_id] = stock - quantity
        total,order_id = order.process_order(quantity)
        self.notification.notify(customer_email,order_id,total)
        # Responsibility 3: Update inventory
        

        # Responsibility 4: Send notification
        

# TODO: Refactor into OrderProcessor, InventoryManager, and NotificationService.

if __name__ == "__main__":
    # After refactoring, usage should look like:
    inventory = InventoryManager()
    notifications = NotificationService()
    processor = OrderProcessor(inventory, notifications)
    processor.place_order("LAPTOP", 2, "alice@example.com")
