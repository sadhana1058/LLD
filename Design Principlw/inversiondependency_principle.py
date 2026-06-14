from abc import ABC,abstractmethod
class Database(ABC):
    @abstractmethod
    def insert(self, table: str, data: str):
        pass
    @abstractmethod
    def query(self, table: str, id: str):
       pass

class MySQLDatabase(Database):
    def insert(self, table: str, data: str) -> None:
        print(f"MySQL: Inserting into {table} -> {data}")

    def query(self, table: str, id: str) -> str:
        print(f"MySQL: Querying {table} for id {id}")
        return f"{{ id: {id}, item: 'Widget' }}"
class PostgresDatabase(Database):
    def insert(self, table: str, data: str) -> None:
        print(f"PostgreSQL: Inserting into {table} -> {data}")

    def query(self, table: str, id: str) -> str:
        print(f"PostgreSQL: Querying {table} for id {id}")
        return f"{{ id: {id}, item: 'Widget' }}"

class OrderService:
    def __init__(self,database:Database):
        self.database =database

    def place_order(self, order_id: str, order_data: str) -> None:
        print(f"Placing order: {order_id}")
        self.database.insert("orders", order_data)
        print("Order placed successfully.")

    def get_order(self, order_id: str) -> str:
        return self.database.query("orders", order_id)

if __name__ == "__main__":
    mysql =MySQLDatabase()
    postgresql =PostgresDatabase()
    print('--- MySQL ---')
    service1 = OrderService(mysql)
    service1.place_order("ORD-001", "{ item: 'Widget', qty: 3 }")
    order = service1.get_order("ORD-001")
    print(f"Order: {order}")
    print()
    print('--- PostgreSQL ---')
    service2 = OrderService(postgresql)
    service2.place_order("ORD-001", "{ item: 'Widget', qty: 3 }")
    order = service2.get_order("ORD-001")
    print(f"Order: {order}")

# TODO: Create a Database ABC with insert() and query() methods.
# TODO: Make MySQLDatabase implement the interface.
# TODO: Create a PostgresDatabase that prints "PostgreSQL: ..." instead of "MySQL: ...".
# TODO: Refactor OrderService to accept a Database via its constructor.