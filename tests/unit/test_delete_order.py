from app.application.use_cases.delete_order import DeleteOrder
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


def test_delete_order():
    repo = FakeOrderRepository()
    order = Order("1", "Test", 50)
    repo.save(order)

    use_case = DeleteOrder(repo)
    use_case.execute("1")

    assert repo.get_by_id("1") is None
