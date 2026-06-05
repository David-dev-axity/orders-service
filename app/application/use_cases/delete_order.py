from app.domain.repositories.order_repository import OrderRepository


class DeleteOrder:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: str) -> None:
        self.repository.delete(order_id)
