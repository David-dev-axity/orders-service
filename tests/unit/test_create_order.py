import pytest
from app.application.use_cases.create_order import CreateOrder
from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository


class FakeOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = []

    def save(self, order: Order) -> Order:
        self.orders.append(order)
        return order

    def get_by_id(self, order_id: str):
        return None

    def list(self):
        return self.orders

    def delete(self, order_id: str):
        pass


def test_create_order_success():
    repository = FakeOrderRepository()
    use_case = CreateOrder(repository)

    order = use_case.execute("David", 100.0)

    assert order.id is not None
    assert order.customer_name == "David"
    assert order.total_amount == 100.0
    assert len(repository.orders) == 1
