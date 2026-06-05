from app.domain.repositories.order_repository import OrderRepository
from app.domain.entities.order import Order


class GetOrder:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: str) -> Order | None:
        return self.repository.get_by_id(order_id)
