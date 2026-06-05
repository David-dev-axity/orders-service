from app.domain.repositories.order_repository import OrderRepository
from app.domain.entities.order import Order


class ListOrders:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self) -> list[Order]:
        return self.repository.list()
