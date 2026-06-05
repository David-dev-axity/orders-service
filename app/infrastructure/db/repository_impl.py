from sqlalchemy.orm import Session
from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository
from app.infrastructure.db.models import OrderModel


class SqlAlchemyOrderRepository(OrderRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, order: Order) -> Order:
        db_order = OrderModel(
            id=order.id,
            customer_name=order.customer_name,
            total_amount=order.total_amount,
        )

        self.session.add(db_order)
        self.session.commit()
        self.session.refresh(db_order)

        return order

    def get_by_id(self, order_id: str) -> Order | None:
        db_order = (
            self.session.query(OrderModel).filter(OrderModel.id == order_id).first()
        )

        if not db_order:
            return None

        return Order(
            id=db_order.id,
            customer_name=db_order.customer_name,
            total_amount=db_order.total_amount,
        )

    def list(self) -> list[Order]:
        db_orders = self.session.query(OrderModel).all()

        return [
            Order(
                id=o.id,
                customer_name=o.customer_name,
                total_amount=o.total_amount,
            )
            for o in db_orders
        ]

    def delete(self, order_id: str) -> None:
        db_order = (
            self.session.query(OrderModel).filter(OrderModel.id == order_id).first()
        )

        if db_order:
            self.session.delete(db_order)
            self.session.commit()
