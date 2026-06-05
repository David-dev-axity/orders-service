from app.application.use_cases.list_orders import ListOrders
from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository


class FakeOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def save(self, order: Order) -> Order:
        self.orders[order.id] = order
        return order

    def get_by_id(self, order_id: str):
        return self.orders.get(order_id)

    def list(self):
        return list(self.orders.values())

    def delete(self, order_id: str):
        self.orders.pop(order_id, None)


def test_list_orders_returns_all_orders():
    repo = FakeOrderRepository()

    repo.save(Order("1", "A", 10))
    repo.save(Order("2", "B", 20))

    use_case = ListOrders(repo)

    result = use_case.execute()

    assert len(result) == 2
    assert result[0].customer_name == "A"
    assert result[1].customer_name == "B"
