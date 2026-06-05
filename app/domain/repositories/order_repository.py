from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.order import Order


class OrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        pass

    @abstractmethod
    def list(self) -> List[Order]:
        pass

    @abstractmethod
    def delete(self, order_id: str) -> None:
        pass
