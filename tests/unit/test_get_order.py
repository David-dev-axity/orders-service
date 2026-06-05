from app.application.use_cases.get_order import GetOrder
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


def test_get_order_success():
    repo = FakeOrderRepository()
    order = Order("1", "David", 150.0)
    repo.save(order)

    use_case = GetOrder(repo)

    result = use_case.execute("1")

    assert result is not None
    assert result.id == "1"
    assert result.customer_name == "David"


def test_get_order_not_found():
    repo = FakeOrderRepository()
    use_case = GetOrder(repo)

    result = use_case.execute("999")

    assert result is None
