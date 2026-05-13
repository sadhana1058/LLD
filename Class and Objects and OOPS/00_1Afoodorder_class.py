class Item:
    def __init__(self, item_id, item_name, price):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price



class Food_Order:
    def __init__(self, order_Id):    
        self.order_Id =order_Id
        self.itemId = 0
        self.orderTotal=0
        self.status="Not Placed"
    
    def addItem(self, itemId):
        if self.status=="Placed":
            print("Cannot modify a placed order.")
            return
        self.orderTotal += itemId.price
        
    def placeOrder(self):
        self.status = "Placed"

item1 =Item(1,"sugar", 10)
item2 =Item(1,"eggs", 100)
ord1 = Food_Order(1)
ord1.addItem(item1)
ord1.addItem(item2)
print(ord1.orderTotal)