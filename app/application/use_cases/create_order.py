from uuid import uuid4
from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository


class CreateOrder:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, customer_name: str, total_amount: float) -> Order:
        order = Order(
            id=str(uuid4()),
            customer_name=customer_name,
            total_amount=total_amount,
        )

        return self.repository.save(order)
